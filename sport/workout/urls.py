from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),  # Главная страница приложения
    path('program/<int:pk>/', views.workout_detail, name='workout_detail'),  # Страница подробностей программы
    path('program/<int:pk>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('program/<int:pk>/remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),
]

