from django.urls import path
from .views import (
    user_list, user_detail,
    project_list, project_detail,
    task_list, task_detail,
    comment_list, comment_detail
)

urlpatterns = [

    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('projects/', project_list, name='project_list'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/', task_list, name='task_list'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),
    path('tasks/<int:task_id>/comments/', comment_list, name='comment_list'),
    path('comments/<int:pk>/', comment_detail, name='comment_detail'),
]
