from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('reviews/', include('reviews.urls')),
    path('', views.index, name='home'),
   # path('', views.record, name='record'),
    path('accounts/', include('accounts.urls')),
    path('faq/',views.faq, name='faq'),
    path('records/', include('records.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)