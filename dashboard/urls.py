from django.urls import path

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^students/$', views.StudentListView.as_view(), name='students'),
]
