
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path('basket/', include('basket.urls', namespace='basket')),
    path('account/', include('account.urls', namespace='account')),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)