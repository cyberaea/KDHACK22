from django.db import models

# Create your models here.
# дата/время название описание тип зал оборудование фио телефон email
# стулья телевизоры короич столы белые столы бежевые столы журнальные столы вешалки диван 2хместный стулья барный колонки микрофона микшер
class Booking(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50)
    hall = models.IntegerField()
    
    chairs = models.IntegerField(default=0)
    bar_stools = models.IntegerField(default=0)
    TVs = models.IntegerField(default=0)
    brown_tables = models.IntegerField(default=0)
    white_tables = models.IntegerField(default=0)
    beige_tables = models.IntegerField(default=0)
    journal_tables = models.IntegerField(default=0)
    bebra_trees = models.IntegerField(default=0)
    sofas = models.IntegerField(default=0)
    speakers = models.IntegerField(default=0)
    mic = models.IntegerField(default=0)
    mixer = models.IntegerField(default=0)

    approved = models.BooleanField(default=False)

class User(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=64)

