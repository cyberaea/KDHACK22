from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')