from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("sport-admin/", admin.site.urls),
    path('', include('post.urls', namespace='post')),
    path('dashboard/', include('core.urls', namespace='home'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

