from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw, ImageFont
from pdf2image import convert_from_path
from django.core.files.base import ContentFile
from io import BytesIO
import os


class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
    ]

    SERVICE_CHOICES = [
        ('presentation', 'Presentation'),
        ('essay', 'Essay'),
        ('report', 'Report'),
        ('poster', 'Poster'),
    ]

    DELIVERY_CHOICES = [
        ('standard', 'Standard'),
    ]

    PRICES = {
        ('presentation', 'standard'): 300,
        ('essay', 'standard'): 200,
        ('report', 'standard'): 350,
        ('poster', 'standard'): 150,
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    topic = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    delivery_type = models.CharField(max_length=20, default='standard')
    slides = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_paid = models.BooleanField(default=False)

    content_file = models.FileField(upload_to='orders/files/', blank=True, null=True)
    content_link = models.URLField(blank=True, null=True)
    content_note = models.TextField(blank=True)

    preview_image = models.ImageField(
        upload_to='orders/previews/',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.price = self.PRICES.get((self.service, self.delivery_type), 0)

        super().save(*args, **kwargs)

        # Preview yarat və watermark əlavə et
        if self.content_file and not self.preview_image:
            try:
                # PDF-dən ilk səhifəni şəkilə çevir
                pages = convert_from_path(
                    self.content_file.path,
                    first_page=1,
                    last_page=1,
                    dpi=180
                )
                image = pages[0]

                # ================= WATERMARK =================
                draw = ImageDraw.Draw(image)
                
                # Font (əgər sistemdə yoxdursa default istifadə olunur)
                try:
                    font = ImageFont.truetype("arial.ttf", 60)  # Böyük watermark
                except:
                    font = ImageFont.load_default()

                # Watermark mətni
                watermark_text = "© Academic Excellence - Sample Only"
                
                # Mətnin ölçüsünü al
                bbox = draw.textbbox((0, 0), watermark_text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]

                # Şəklin mərkəzində yerləşdir (diaqonal)
                x = (image.width - text_width) // 2
                y = (image.height - text_height) // 2

                # Yarı şəffaf qara rəng
                draw.text((x, y), watermark_text, fill=(255, 255, 255, 80), font=font, stroke_width=3, stroke_fill=(0,0,0,100))

                # ================= WATERMARK SON =================

                buffer = BytesIO()
                image.save(buffer, format='JPEG', quality=82)

                filename = os.path.splitext(os.path.basename(self.content_file.name))[0] + "_preview.jpg"

                self.preview_image.save(
                    filename,
                    ContentFile(buffer.getvalue()),
                    save=False
                )

                super().save(update_fields=['preview_image'])

            except Exception as e:
                print("Preview error:", str(e))

    def __str__(self):
        return f"{self.user.username} - {self.service}"