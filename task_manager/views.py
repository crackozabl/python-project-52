from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def test_rollbar(request):
    a = None
    a.hello()
    return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('You are logged in.')


class UserLogoutView(LogoutView):
    template_name = 'logout.html'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out.'))
        return super().dispatch(request, *args, **kwargs)
