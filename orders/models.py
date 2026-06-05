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

        if self.content_file and not self.preview_image:
            print(f"🔄 Preview generation started for Order #{self.pk}")
            try:
                pages = convert_from_path(
                    self.content_file.path,
                    first_page=1,
                    last_page=1,
                    dpi=150
                )
                image = pages[0].convert("RGB")

                # Sadə watermark (font problemi olmasın deyə)
                draw = ImageDraw.Draw(image)
                font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
                font = ImageFont.truetype(font_path, 60)

                watermark_text = "SAMPLE - FULL VERSION AFTER PAYMENT"
                bbox = draw.textbbox((0, 0), watermark_text, font=font)
                x = (image.width - (bbox[2] - bbox[0])) // 2
                y = (image.height - (bbox[3] - bbox[1])) // 2

                draw.text((x, y), watermark_text, fill=(255, 255, 255, 90), font=font)

                buffer = BytesIO()
                image.save(buffer, format='JPEG', quality=85)

                filename = os.path.splitext(os.path.basename(self.content_file.name))[0] + "_preview.jpg"

                self.preview_image.save(filename, ContentFile(buffer.getvalue()), save=False)
                super().save(update_fields=['preview_image'])

                print(f"✅ SUCCESS: Preview created for Order #{self.pk}")

            except Exception as e:
                print(f"❌ Preview ERROR: {str(e)}")
                import traceback
                traceback.print_exc()

    def __str__(self):
        return f"{self.user.username} - {self.service}"