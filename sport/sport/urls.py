from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('workout/', include('workout.urls')),
    path('reviews/', include('reviews.urls')),
    path('exercises/', include('exercises.urls')),
    path('records/', include('records.urls')),
]
if settings.DEBUG:  # Это нужно только для разработки (не используйте в продакшн!)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)