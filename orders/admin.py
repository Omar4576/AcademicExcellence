from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'status', 'created_at']
    list_filter = ['status', 'service']
    list_editable = ['status']