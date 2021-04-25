from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class LandingPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "landing-page.html"
    login_url = 'user/login'

