from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from .models import Student

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = Student.objects.all().aggregate(Avg('gpa'))

        context['students'] = Student.objects.all()
        context['juniors'] = Student.objects.filter(year='Junior')
        context['seniors'] = Student.objects.filter(year='Senior')
        context['sophomores'] = Student.objects.filter(year='Sophomore')
        return context
