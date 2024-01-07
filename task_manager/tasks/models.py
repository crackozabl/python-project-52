from django.db import models
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status', verbose_name=_('Status'))
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='author')
    assignee = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='assignee', verbose_name=_('Assignee'))

    labels = models.ManyToManyField(Label, related_name='labels', verbose_name=_('Labels'), blank=True)

    def __str__(self):
        return self.name
