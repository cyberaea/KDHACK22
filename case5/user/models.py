from django.db import models

# Create your models here.
# дата/время название описание тип зал оборудование фио телефон email
# стулья телевизоры короич столы белые столы бежевые столы журнальные столы вешалки диван 2хместный стулья барный колонки микрофона микшер
class User(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50)
    hall = models.IntegerField()
    
    chairs = models.IntegerField()
    bar_stools = models.IntegerField()
    TVs = models.IntegerField()
    brown_tables = models.IntegerField()
    white_tables = models.IntegerField()
    beige_tables = models.IntegerField()
    journal_tables = models.IntegerField()
    bebra_trees = models.IntegerField()
    sofas = models.IntegerField()
    speakers = models.IntegerField()
    mic = models.IntegerField()
    mixer = models.IntegerField()

    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'