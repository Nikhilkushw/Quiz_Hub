from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('create/', views.quiz_create, name='quiz_create'),
    path('<int:quiz_id>/edit/', views.quiz_edit, name='quiz_edit'),
    path('<int:quiz_id>/delete/', views.quiz_delete, name='quiz_delete'),
]