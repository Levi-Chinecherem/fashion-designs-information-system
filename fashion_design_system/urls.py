# fashion_design_system/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('designs.urls')),
    path('scheduling/', include('scheduling.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)