from django.urls import path

from .views import (
    TaskListViewActive,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskListViewDone,
    TaskListViewAll,
)

app_name = 'task'

urlpatterns = [
    path('', TaskListViewActive.as_view(), name='task-list'),
    path('tasks-done/', TaskListViewDone.as_view(), name='task-list-done'),
    path('tasks-all/', TaskListViewAll.as_view(), name='task-list-all'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('new/', TaskCreateView.as_view(), name='task-create'),

]