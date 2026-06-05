from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
]

# ==================== MEDIA & STATIC ====================

# Media fayllar (preview şəkillər, uploaded PDF-lər) — həmişə aktiv olsun
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Static fayllar üçün (yalnız DEBUG=True olduqda əlavə et)
# Çünki WhiteNoise production-da onları idarə edir
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)