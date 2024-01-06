from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from django.utils.translation import gettext as _


# Create your views here.


class LabelListView(ListView):
    model = Label
    template_name = 'labels/list.html'


class LabelCreateView(CreateView):
    model = Label
    template_name = 'labels/create.html'
    success_url = '/labels/'
    fields = ('name',)


class LabelUpdateView(UpdateView):
    model = Label
    template_name = 'labels/update.html'
    success_url = '/labels/'
    fields = ('name',)


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = '/labels/'
