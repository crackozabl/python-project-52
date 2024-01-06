from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
# from task_manager.users.models import User
from django.views.generic import \
    ListView, CreateView, DeleteView, UpdateView
# from django.views.generic.edit import DeleteView


class UserListView(ListView):
    model = get_user_model()
    template_name = 'users/list.html'


class UserCreateView(CreateView):
    model = get_user_model()
    template_name = 'users/create.html'
    fields = ('username', 'first_name', 'last_name', 'password')
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
