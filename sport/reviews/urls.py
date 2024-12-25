from django.urls import path
from . import views

urlpatterns = [
    path('program/<int:program_pk>/reviews/', views.program_reviews, name='program_reviews'),
    path('program/<int:program_pk>/add_review/', views.add_review, name='add_review'),
    path('all_reviews/', views.all_reviews, name='all_reviews'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('all_reviews/<int:review_id>/delete/', views.delete_all_review, name='delete_all_review'),

]
