from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'status', 'is_paid', 'created_at']
    list_filter = ['status', 'service', 'is_paid']
    list_editable = ['status', 'is_paid']
    fields = ['user', 'service', 'topic', 'deadline', 'delivery_type', 
              'slides', 'status', 'is_paid', 'content_file', 'content_link', 'content_note', 'notes']