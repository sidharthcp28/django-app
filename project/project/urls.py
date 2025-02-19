from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('courses.urls')),  # Include URLs from the courses app
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
