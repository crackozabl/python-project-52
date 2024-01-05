from django.contrib.auth import get_user_model
from django.views.generic import ListView


class UserListView(ListView):
    model = get_user_model()
    template_name = 'users/list.html'