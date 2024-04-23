from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/', views.project_todo_list, name='project_todo_list'),
    path('projects/<int:project_id>/update/', views.project_update, name='project_update'),
    path('projects/<int:project_id>/delete/', views.project_delete, name='project_delete'),
    path('projects/<int:project_id>/todos/create/', views.todo_create, name='todo_create'),
    path('projects/<int:project_id>/todos/<int:todo_id>/update/', views.todo_update, name='todo_update'),
    path('projects/<int:project_id>/todos/<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
]
