from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return HttpResponse("Hello world")

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
