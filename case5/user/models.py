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
    
    chairs = models.CharField(max_length=20)
    bar_stools = models.CharField(max_length=20)
    TVs = models.CharField(max_length=20)
    brown_tables = models.CharField(max_length=20)
    white_tables = models.CharField(max_length=20)
    beige_tables = models.CharField(max_length=20)
    journal_tables = models.CharField(max_length=20)
    bebra_trees = models.CharField(max_length=20)
    sofas = models.CharField(max_length=20)
    speakers = models.CharField(max_length=20)
    mic = models.CharField(max_length=20)
    mixer = models.CharField(max_length=20)

    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.title