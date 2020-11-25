from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from .models import Student, Course
from .forms import StudentForm, EnrollForm

class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = Student.objects.all().aggregate(Avg('gpa'))

        context['students'] = Student.objects.all()
        context['juniors'] = Student.objects.filter(year='Junior')
        context['seniors'] = Student.objects.filter(year='Senior')
        context['sophomores'] = Student.objects.filter(year='Sophomore')
        return context


class EnrollmentView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = "enrollment_base.html"

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = {}

        context['students'] = Student.objects.all()
        return context


class StudentListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Student
    template_name = 'students.html'

class CourseListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Course
    template_name = 'courses.html'

class StudentDetailView(LoginRequiredMixin, DetailView): 
    model = Student 
    template_name = 'enrollment.html'
    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = super().get_context_data(**kwargs)

        context['students'] = Student.objects.all()
        context['courses'] = Course.objects.all()
        return context

 
def SelectStudentView(request):
 
    if request.method == 'POST':
        form = StudentForm(request.POST)
 
        if form.is_valid():
            pk = form.cleaned_data['pk']
            return redirect('enrollment_pk', pk=pk)
        else:
            return redirect('enrollment')
    else:
        return redirect('enrollment')


def get_course(form, number):
    pk = form.cleaned_data['course' + str(number)]
    if pk == -1:
        return None
    return Course.objects.get(pk=pk)


def EnrollView(request, pk=None):
 
    if request.method == 'POST':
        form = EnrollForm(request.POST)
 
        if form.is_valid():
            student = Student.objects.get(id=pk)
            student.course1 = get_course(form, 1)
            student.course2 = get_course(form, 2)
            student.course3 = get_course(form, 3)
            student.save()
            return redirect('enrollment_pk', pk=pk)
        else:
            print(f'form {form} is invalid')
            return redirect('enrollment')
    else:
        return redirect('enrollment')
