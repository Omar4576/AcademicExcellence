from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/orders/', views.order_list, name='order_list'),
    path('dashboard/orders/new/', views.order_new, name='order_new'),
    path('dashboard/orders/<int:pk>/', views.order_detail, name='order_detail'),
    path(
    'dashboard/orders/<int:pk>/download/',
    views.download_order_file,
    name='download_order_file'
),
]