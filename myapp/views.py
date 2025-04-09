from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Welcome to the Task Management API'})


# Create Task
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# List Tasks
class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Retrieve Task
class TaskDetailView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Update Task
class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Delete Task
class TaskDeleteView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
