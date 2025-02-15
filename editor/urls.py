from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('main_app.urls')),  # CKEditor URLs
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # CKEditor URLs
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
