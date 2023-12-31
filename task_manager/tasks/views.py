import django.forms
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from task_manager.tasks.models import Task
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from django_filters import FilterSet
from django_filters.filters import BooleanFilter, ModelChoiceFilter
from task_manager.labels.models import Label
from task_manager.mixins import AuthRequireMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect


class TaskAuthorTestMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user != self.get_object().author:
            self.raise_exception = False
            self.permission_denied_message = \
                ('You cannot delete non-your task!')

            return False
        else:
            return True

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('tasks:list'))


class TaskFilter(FilterSet):
    self_tasks = BooleanFilter(
        widget=django.forms.CheckboxInput,
        field_name='author',
        method='filter_self_tasks',
        label=_('Only their own tasks'),
    )

    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('Label'),
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'self_tasks']


class TaskListView(AuthRequireMixin, FilterView):
    model = Task
    template_name = 'tasks/list.html'
    filterset_class = TaskFilter


class TaskCreateView(AuthRequireMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'tasks/create.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'executor', 'labels')
    success_message = _('Task created successfully')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailsView(AuthRequireMixin, DetailView):
    model = Task
    template_name = 'tasks/details.html'


class TaskUpdateView(AuthRequireMixin, SuccessMessageMixin, UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    success_url = '/tasks/'
    fields = ('name', 'description', 'status', 'executor', 'labels')
    success_message = _('Task updated successfully')


class TaskDeleteView(AuthRequireMixin, SuccessMessageMixin, TaskAuthorTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'
    success_message = _('Task deleted successfully')
