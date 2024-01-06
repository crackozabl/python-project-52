from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/list.html'


class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'statuses/create.html'
    success_url = '/statuses/'
    fields = ('name',)
    success_message = _('Status created successfully')


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    success_url = '/statuses/'
    fields = ('name',)
    success_message = _('Status updated successfully')


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = '/statuses/'
    success_message = _('Status deleted successfully')
