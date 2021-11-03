from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admissionform/', views.admissionForm, name='admissionForm'),
    path('login/', views.loginPage, name='loginPage'),
    path('contact/', views.contact, name='contact'),
    path('forum/', views.forum, name="forum"),
    path('process_admission_form/', views.processAdmisssionForm,name="process_admission_form"),
    path('process_contact_form/', views.processContact, name="process_contact")
]