from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = "index.html"
