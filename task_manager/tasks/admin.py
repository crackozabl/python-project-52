from django.contrib import admin
from task_manager.tasks.models import Task


class TaskModelAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Task, TaskModelAdmin)
