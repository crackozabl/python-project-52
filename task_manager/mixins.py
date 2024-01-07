from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class AuthRequireMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _('You are not logged in! Please sign in.')
        # self.permission_denied_url = self.get_login_url()
        # self.permission_denied_url = reverse_lazy('login')
        self.login_url = reverse_lazy('login')
        self.redirect_field_name = ''
        # print(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)
