from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f"{self.user.username} - {self.service}"