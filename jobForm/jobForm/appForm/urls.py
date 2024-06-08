from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobForm, name='job-form'),
]