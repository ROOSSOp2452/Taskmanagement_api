from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description', 'user__username')
