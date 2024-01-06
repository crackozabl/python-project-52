from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from task_manager.tasks.models import Task
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'tasks/create.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'assignee', 'labels')
    success_message = _('Task created successfully')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailsView(DetailView):
    model = Task
    template_name = 'tasks/details.html'


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'assignee', 'labels')
    success_message = _('Task updated successfully')


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'
    success_message = _('Task deleted successfully')
