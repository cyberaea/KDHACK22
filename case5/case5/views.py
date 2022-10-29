from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')

def booking(request):
    return render(request, 'booking.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def singup(request):
    return render(request, 'singup.html')