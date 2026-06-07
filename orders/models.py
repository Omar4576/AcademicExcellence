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
                    dpi=130
                )
                image = pages[0].convert("RGB")
                draw = ImageDraw.Draw(image)
                w, h = image.size

                # ========== Ağır Blur (Ən güclü hissə) ==========
                from PIL import ImageFilter
                
                # Aşağı 62% hissəni çox ağır blur et
                blur_zone = image.crop((0, int(h * 0.38), w, h))
                blurred = blur_zone.filter(ImageFilter.GaussianBlur(radius=24))  # 22 → 24 etdim
                image.paste(blurred, (0, int(h * 0.38)))

                # Üst hissəyə yüngül blur
                upper = image.crop((0, 0, w, int(h * 0.42)))
                upper_blurred = upper.filter(ImageFilter.GaussianBlur(radius=5))
                image.paste(upper_blurred, (0, 0))

                # ========== Watermark ==========
                try:
                    font = ImageFont.truetype("arial.ttf", 58)
                except:
                    font = ImageFont.load_default()

                text = "SAMPLE - FULL VERSION AFTER PAYMENT"
                bbox = draw.textbbox((0, 0), text, font=font)
                x = (w - (bbox[2] - bbox[0])) // 2
                y = (h - (bbox[3] - bbox[1])) // 2

                # Daha güclü watermark
                draw.text((x, y), text, fill=(255, 255, 255, 80), 
                         font=font, stroke_width=6, stroke_fill=(0, 0, 0, 220))

                # Buffer və yadda saxlama
                buffer = BytesIO()
                image.save(buffer, format='JPEG', quality=65, optimize=True)

                filename = os.path.splitext(os.path.basename(self.content_file.name))[0] + "_preview.jpg"

                self.preview_image.save(filename, ContentFile(buffer.getvalue()), save=False)
                super().save(update_fields=['preview_image'])

                print(f"✅ Protected Preview created for Order #{self.pk}")

            except Exception as e:
                print(f"❌ Preview ERROR: {str(e)}")
                import traceback
                traceback.print_exc()
                
    def __str__(self):
        return f"{self.user.username} - {self.service}"