from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.labels.models import Label
from task_manager.mixins import AuthRequireMixin


class LabelListView(AuthRequireMixin, ListView):
    model = Label
    template_name = 'labels/list.html'


class LabelCreateView(SuccessMessageMixin, AuthRequireMixin, CreateView):
    model = Label
    template_name = 'labels/create.html'
    success_url = '/labels/'
    fields = ('name',)
    success_message = _('Label created successfully')


class LabelUpdateView(SuccessMessageMixin, AuthRequireMixin, UpdateView):
    model = Label
    template_name = 'labels/update.html'
    success_url = '/labels/'
    fields = ('name',)
    success_message = _('Label updated successfully')


class LabelDeleteView(SuccessMessageMixin, AuthRequireMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = '/labels/'
    success_message = _('Label deleted successfully')
