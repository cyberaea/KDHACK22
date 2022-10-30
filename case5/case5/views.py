from threading import BrokenBarrierError
from xmlrpc.server import MultiPathXMLRPCServer
from django.forms import CharField
from django.shortcuts import redirect, render
from user.models import User
from user.models import Booking
from http import cookies
import datetime

def index(request):
    return render(request, 'index.html')

def check(book_by_time, date, time, timeend):
    for i in range(1, book_by_time.count() + 1):
        el = book_by_time.get(id=i)
        if time <= el.time <= timeend or time <= el.timeend <= timeend or el.time <= time and el.timeend >= timeend:
            return False
    return True 

def booking(request):
    if request.method == 'POST':
        dt = request.POST.get('date').split('-')
        dt = tuple(map(int, dt))
        a1, b1, c1 = dt[0], dt[1], dt[2]
        date = datetime.date(a1, b1, c1)

        t = request.POST.get('time').split(':')
        t = tuple(map(int, t))
        a2, b2 = t[0], t[1]
        time = datetime.time(a2, b2)

        te = request.POST.get('timeend').split(':')
        te = tuple(map(int, te))
        a3, b3 = te[0], te[1]
        timeend = datetime.time(a3, b3)

        #book_to_delete = Booking().objects.filter(approved=0)

        hall = request.POST.get('hall')
        book_by_hall = Booking.objects.filter(hall__iexact=hall)
        book_by_date = book_by_hall.filter(date__iexact=date)
        book_by_time = book_by_date.filter(approved__iexact=1)
        if check(book_by_time, date, time, timeend):
            book = Booking()

            book.date = datetime.date(a1, b1, c1)

            book.time = datetime.time(a2, b2)

            book.timeend = datetime.time(a3, b3)

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
            book.user_id = int(request.COOKIES['id'])
            book.save()
    return render(request, 'booking.html')


def adminpanel(request):
    user = User
    x = int(request.COOKIES['id'])
    u = user.objects.filter(id__iexact=x)
    bs = Booking.objects.order_by('date')
    if u.latest('login').is_admin:
        if request.method == 'POST':
            x2 = request.POST.get('iuda')
            print(x2)
            boob = Booking.objects.get(id=int(x2))
            if request.POST.get('otkl'):
                boob.delete()
            elif request.POST.get('prin'):
                boob.approved = 1
                boob.save()
        ctx = {
            'bs': bs,
            'us': u,
        }
        return render(request, 'adminpanel.html', ctx)
    else:
        return render(request, 'adminpanel_poshel_von.html')

def home(request):
    return render(request, 'home.html')

def get_model_fields(model):
    return model._meta.fields


def profile(request):
    
    genres = {
        '1': 'Спортивное мероприятие',
        '2': 'Музыкальное мероприятие',
        '3': 'Конференция',
        '4': 'Выставка',
        '5': 'Мастер класс / тренинг',
        '6': 'Праздник',
        '7': 'Банкет',
        '8': 'Благотворительная акция',
        '9': 'Другое'
    }

    halls = {
        '1': 'Большой зал',
        '2': 'Большой танцевальный зал',
        '3': 'Зал бочки',
        '4': 'Малый ситцевый зал',
        '5': 'Ситцевая',
    }

    x = int(request.COOKIES['id'])
    u = User.objects.filter(id__iexact=x)
    un = u.latest('login').name
    bs = Booking.objects.filter(user_id__iexact=x).order_by('date')
    # print(un)
    for b in bs:
        print(b.type)
    ctx = {
        'bs': bs,
        'un': un,
        'genres': genres,
        'hall': halls,
    }


    return render(request, 'profile.html', ctx)

def login(request):
    rsn = render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = User.objects.filter(login__iexact=username)
        if not (user.count() == 0):
            # print(user.latest('login').id)
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
        if user.password == '123': 
            user.is_admin = 1
        user.save()
        rsn.set_cookie('id', str(user.id), max_age=315336000)
        # return redirect('/profile')
    return rsn
