from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
from .models import *
# Create your views here.

def home(request):
    context={}
    return render(request, 'main.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            id = request.POST.get('id')
            pin = request.POST.get('pin')

            user = authenticate(request, username=id, password=pin)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'id or pin is incorrect')
                return render(request, 'home.html', {})
        context = {}
        return render(request, 'login.html', context)

def admissionForm(request):
    context = {}
    return render(request, 'admission.html', context)


def processAdmisssionForm(request):
    data = json.loads(request)
    AdmissionForm.objects.create(
        firstname = data['form']['firstname'],
        lastname = data['form']['lastname'],
        middlename = data['form']['middlename'],
        dob = data['form']['dob'],
        gender = data['form']['gender'],
        hometown = data['form']['hometown'],
        religion = data['form']['religion'],
        email = data['form']['email'],
        picture = data['form']['picture'],
        disability = data['form']['disability'],
        disability_info = data['form']['disability_info'],
        transportation = data['form']['transportation'],

        parent_name = data['form']['parent_name'],
        parent_address_line = data['form']['parent_address_line'],
        parent_occupation = data['form']['occupation'],
        number = data['form']['contact'],
        parent_email = data['form']['parent_email'],
    )
    return JsonResponse("Form sent", safe=False)

def processContact(request):
    data = json.loads(request)
    Contact.objects.create(
        firstname = data['form']['firstname'],
        lastname = data['form']['lastname'],
        email = data['form']['email'],
        phone = data['form']['phone'],
        message = data['form']['message']
    )
    return JsonResponse("form has been sent", safe=False)


def forum(request):
    context = {}
    return render(request, "forum.html", context)

def contact(request):
    context = {}
    return render(request, "Contact.html", context)

