from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


def index(request):
    return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    template_name = 'logout.html'
