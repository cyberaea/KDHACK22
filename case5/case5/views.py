from threading import BrokenBarrierError
from xmlrpc.server import MultiPathXMLRPCServer
from django.forms import CharField
from django.shortcuts import redirect, render
from user.models import User
from user.models import Booking
from http import cookies


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')

def booking(request):
    book = Booking()
    if request.method == 'POST':
        book.date = request.POST.get('date')
        book.time = request.POST.get('time')
        book.timeend = request.POST.get('timeend')
        book.title = request.POST.get('event_name')
        book.description = request.POST.get('event_disc')
        book.type = request.POST.get('event_type')
        book.hall = request.POST.get('hall')
        book.chairs = request.POST.get('chair')
        book.TVs = request.POST.get('LG')
        book.brown_tables = request.POST.get('brown_table')
        book.white_tables = request.POST.get('white_table')
        book.bebra_trees = request.POST.get('bebra')
        book.journal_tables = request.POST.get('jour_table')
        book.sofas = request.POST.get('sofa')
        book.bar_stools = request.POST.get('bar_chair')
        book.speakers = request.POST.get('stereo')
        book.mic = request.POST.get('radio')
        book.mixer = request.POST.get('mixer')
        book.beige_tables = request.POST.get('beig_table')
        book.tables =  request.POST.get('table')
        book.save()
    return render(request, 'booking.html')

def adminpanel(request):
    return render(request, 'adminpanel.html')

def home(request):
    return render(request, 'home.html')

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
