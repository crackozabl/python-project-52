from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from task_manager.tasks.models import Task
from django.utils.translation import gettext as _

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/create.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'assignee', 'labels')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailsView(DetailView):
    model = Task
    template_name = 'tasks/details.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'assignee', 'labels')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'
