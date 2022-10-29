from django.shortcuts import render
from user.models import User


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
    if request.method == 'POST':
        user = User()
        user.login = request.POST.get('login')
        user.name =  request.POST.get('name')
        user.tg =  request.POST.get('tg')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()
    return render(request, 'singup.html')
