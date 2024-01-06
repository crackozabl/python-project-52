from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from task_manager.tasks.models import Task

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/create.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'labels')


class TaskDetailsView(DetailView):
    model = Task
    template_name = 'tasks/details.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'labels')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'
# Create your views here.
