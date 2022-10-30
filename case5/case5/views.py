from django.shortcuts import render, redirect
from user.models import User
from http import cookies


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')

def booking(request):
    return render(request, 'booking.html')

def profile(request):
    user = User
    x = int(request.COOKIES['id'])
    u = user.objects.filter(id__iexact=x)
    ctx = {
        'user': u.latest('login').name,
    }
    return render(request, 'profile.html', ctx)

def login(request):
    rsn = render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = User.objects.filter(login__iexact=username)
        if not (user.count() == 0):
            print(user.latest('login').id)
            if username == user.latest('login').login and password == user.latest('login').password:
                rsn.set_cookie('id', user.latest('login').id, max_age=315336000)
                # return redirect('/profile')
    return rsn

def singup(request):
    user = User()
    ctx = {
        'name': user.name 
    }
    rsn = render(request, 'singup.html', ctx)
    if request.method == 'POST':
        user.login = request.POST.get('login')
        user.name =  request.POST.get('name')
        user.tg = request.POST.get('tg')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()
        rsn.set_cookie('id', str(user.id), max_age=315336000)
        # return redirect('/profile')
    return rsn
