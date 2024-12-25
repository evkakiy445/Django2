from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.records_view, name='records'),
    path('add/', views.add_record_view, name='add_record_view'),
]