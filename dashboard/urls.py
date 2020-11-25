from django.urls import path, re_path

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^students/$', views.StudentListView.as_view(), name='students'),
    url(r'^courses/$', views.CourseListView.as_view(), name='courses'),
    path(r'enrollment/', views.EnrollmentView.as_view(), name='enrollment'),
    path(r'enrollment/select_student', views.SelectStudentView),
    re_path(r'enrollment/[0-9]+/select_student', views.SelectStudentView),
    path(r'enrollment/<int:pk>/', views.StudentDetailView.as_view(), name='enrollment_pk'),
    path(r'enrollment/<int:pk>/enroll', views.EnrollView),
]
