from ctypes.wintypes import LGRPID
from termios import FIOASYNC
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

def profile(request):
    return render(request, 'profile.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(name__icontains=username)
        if not (user.count() == 0):
            if username == user.latest().login and password == user.latest().password:
                pass

    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')

def adminpanel(request):
    return render(request, 'adminpanel.html')

def singup(request):
    if request.method == 'POST':
        user = User()
        user.login = request.POST.get('login')
        user.name =  request.POST.get('name')
        user.tg = request.POST.get('tg')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()
        return redirect('profile')
    return render(request, 'singup.html')
