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
    chairs = models.CharField(max_length=10)
    bar_stools = models.CharField(max_length=10)
    TVs = models.CharField(max_length=10)
    brown_tables = models.CharField(max_length=10)
    white_tables = models.CharField(max_length=10)
    beige_tables = models.CharField(max_length=10)
    journal_tables = models.CharField(max_length=10)
    bebra_trees = models.CharField(max_length=10)
    sofas = models.CharField(max_length=10)
    speakers = models.CharField(max_length=10)
    mic = models.CharField(max_length=10)
    mixer = models.CharField(max_length=10)

    approved = models.BooleanField(default=False)
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
