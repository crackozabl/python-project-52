from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.statuses.models import Status
from task_manager.mixins import AuthRequireMixin


class StatusListView(AuthRequireMixin, ListView):
    model = Status
    template_name = 'statuses/list.html'


class StatusCreateView(SuccessMessageMixin, AuthRequireMixin, CreateView):
    model = Status
    template_name = 'statuses/create.html'
    success_url = '/statuses/'
    fields = ('name',)
    success_message = _('Status created successfully')


class StatusUpdateView(SuccessMessageMixin, AuthRequireMixin, UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    success_url = '/statuses/'
    fields = ('name',)
    success_message = _('Status updated successfully')


class StatusDeleteView(SuccessMessageMixin, AuthRequireMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = '/statuses/'
    success_message = _('Status deleted successfully')
