from django.db import models
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status')
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='author')
    assignee = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='assignee')

    labels = models.ManyToManyField(Label, related_name='labels')

    def __str__(self):
        return self.name
