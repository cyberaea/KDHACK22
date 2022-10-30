from email.policy import default
from django.db import models
import datetime

# Create your models here.
# дата/время название описание тип зал оборудование фио телефон email
# стулья телевизоры короич столы белые столы бежевые столы журнальные столы вешалки диван 2хместный стулья барный колонки микрофона микшер
class Booking(models.Model):
    date = models.DateField(default=datetime.date(1, 1, 1))
    time = models.TimeField(default=datetime.time(0, 0))
    timeend = models.TimeField(default=datetime.time(0, 0))
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50)
    hall = models.IntegerField(default=0)
    chairs = models.CharField(max_length=10)
    bar_stools = models.CharField(max_length=10)
    TVs = models.CharField(max_length=10)
    brown_tables = models.CharField(max_length=10)
    white_tables = models.CharField(max_length=10)
    beige_tables = models.CharField(max_length=10)
    tables = models.CharField(max_length=10)
    journal_tables = models.CharField(max_length=10)
    bebra_trees = models.CharField(max_length=10)
    sofas = models.CharField(max_length=10)
    speakers = models.CharField(max_length=10)
    mic = models.CharField(max_length=10)
    mixer = models.CharField(max_length=10)

    approved = models.BooleanField(default=False)
    user_id = models.IntegerField(default=-1)
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.title

class User(models.Model):
    login = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    tg = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    is_admin = models.BooleanField(default=False)

class Stuff(models.Model):
    chairs = models.CharField(max_length=10, default=str(40+40+5+5+12))
    bar_stools = models.CharField(max_length=10, default='1')
    TVs = models.CharField(max_length=10, default='2')
    brown_tables = models.CharField(max_length=10, default='3')
    white_tables = models.CharField(max_length=10, default='1')
    beige_tables = models.CharField(max_length=10, default='')
    tables = models.CharField(max_length=10, default='7')
    journal_tables = models.CharField(max_length=10, default='2')
    bebra_trees = models.CharField(max_length=10, default='5')
    sofas = models.CharField(max_length=10, default='1')
    speakers = models.CharField(max_length=10, default='2')
    mic = models.CharField(max_length=10, default='1')
    mixer = models.CharField(max_length=10, default='1')