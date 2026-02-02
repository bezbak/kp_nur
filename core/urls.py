from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from settings.views import index, price_page_public

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("p/<slug:slug>/", price_page_public, name="price_page_public"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
