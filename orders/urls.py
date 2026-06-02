from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/orders/', views.order_list, name='order_list'),
    path('dashboard/orders/new/', views.order_new, name='order_new'),
    path('dashboard/orders/<int:pk>/', views.order_detail, name='order_detail'),
]