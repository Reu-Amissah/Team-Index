from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admissionform/', views.admissionForm, name='admissionForm')
]