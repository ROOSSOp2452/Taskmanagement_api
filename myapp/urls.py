from django.urls import path
from .views import home, TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', home, name='home'),  # 👈 root path!
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:id>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:id>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
