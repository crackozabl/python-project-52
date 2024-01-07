from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.labels.models import Label
from task_manager.mixins import AuthRequireMixin
from django.contrib import messages
from django.shortcuts import redirect


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

    def post(self, request, *args, **kwargs):
        if self.get_object().labels.exists():
            messages.error(self.request, _('You cannot delete label with tasks'))
            return redirect(self.success_url)

        return super().post(request, *args, **kwargs)
