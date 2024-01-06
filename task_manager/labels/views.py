from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class LabelListView(ListView):
    model = Label
    template_name = 'labels/list.html'


class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Label
    template_name = 'labels/create.html'
    success_url = '/labels/'
    fields = ('name',)
    success_message = _('Label created successfully')


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'labels/update.html'
    success_url = '/labels/'
    fields = ('name',)
    success_message = _('Label updated successfully')


class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = '/labels/'
    success_message = _('Label deleted successfully')
