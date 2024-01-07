from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import \
    ListView, CreateView, DeleteView, UpdateView
from task_manager.users.forms import UserRegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect


class SelfUserTestMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user != self.get_object():
            self.raise_exception = False
            self.permission_denied_message = \
                ('You cannot change not yourself! Please sign in.')

            return False
        else:
            return True

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('users:list'))


class UserListView(ListView):
    model = get_user_model()
    template_name = 'users/list.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    template_name = 'users/create.html'
    form_class = UserRegistrationForm
    # fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
    success_url = reverse_lazy('login')
    success_message = _('User registred successfully')


class UserUpdateView(SuccessMessageMixin, SelfUserTestMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/update.html'
    form_class = UserRegistrationForm
    # fields = ('first_name', 'last_name', 'username', 'password')
    success_url = reverse_lazy('users:list')
    success_message = _('Пользователь успешно изменен')


class UserDeleteView(SuccessMessageMixin, SelfUserTestMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')
    success_message = _('Пользователь успешно удален')
