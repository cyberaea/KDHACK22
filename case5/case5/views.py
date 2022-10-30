from ctypes.wintypes import LGRPID
from termios import FIOASYNC
from threading import BrokenBarrierError
from xmlrpc.server import MultiPathXMLRPCServer
from django.forms import CharField
from django.shortcuts import redirect, render
from user.models import User
from http import cookies


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')

def booking(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        event_name = request.POST.get('event_name')
        event_disc = request.POST.get('event_disc')
        event_type = request.POST.get('event_type')
        hall = request.POST.get('hall')
        chair = request.POST.get('chair')
        LG = request.POST.get('LG')
        brown_table = request.POST.get('brown_table')
        white_table = request.POST.get('white_table')
        bebra = request.POST.get('bebra')
        jour_table = request.POST.get('jour_table')
        sofa = request.POST.get('sofa')
        bar_chair = request.POST.get('bar_chair')
        stereo = request.POST.get('stereo')
        radio = request.POST.get('radio')
        mixer = request.POST.get('mixer')
        beig_table = request.POST.get('beig_table')
        table =  request.POST.get('table')
        FIO = request.POST.get('FIO')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        
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
