from django.urls import path
from .views import register, CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/profile/', views.profile, name='profile'),
    path('login/profile/add_workout_result/<int:program_pk>/<int:exercise_pk>/', views.add_workout_result, name='add_workout_result'),
    path('login/profile/add_weight_tracking/', views.add_weight_tracking, name='add_weight_tracking'),
    path('add_workout_result/<int:program_pk>/<int:exercise_pk>/', views.add_workout_result, name='add_workout_result'),
    path('profile/delete_workout_result/<int:result_pk>/', views.delete_workout_result, name='delete_workout_result'),
    path('delete_weight/<int:pk>/', views.delete_weight_tracking, name='delete_weight_tracking'),
]

