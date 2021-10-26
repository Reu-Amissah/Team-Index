from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admissionform/', views.admissionForm, name='admissionForm'),
    path('login/', views.loginPage, name='loginPage'),
    path('contact/', views.contact, name='contact'),
    path('forum/', views.forum, name="forum"),
]