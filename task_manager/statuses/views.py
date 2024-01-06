from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from django.utils.translation import gettext as _

# Create your views here.


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/list.html'


class StatusCreateView(CreateView):
    model = Status
    template_name = 'statuses/create.html'
    success_url = '/statuses/'
    fields = ('name',)


class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    success_url = '/statuses/'
    fields = ('name',)


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = '/statuses/'
