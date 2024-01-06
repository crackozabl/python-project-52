from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import \
    ListView, CreateView, DeleteView, UpdateView
from task_manager.users.forms import UserRegistrationForm
# from django.utils.translation import gettext as _


class UserListView(ListView):
    model = get_user_model()
    template_name = 'users/list.html'


class UserCreateView(CreateView):
    model = get_user_model()
    template_name = 'users/create.html'
    form_class = UserRegistrationForm
    # fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView):
    model = get_user_model()
    fields = ('first_name', 'last_name', 'username', 'password')
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')


class UserDeleteView(DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:list')
