from django.db import models

# Create your models here.
# дата/время название описание тип зал оборудование фио телефон email

class User(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50)
    hall = models.IntegerField()
    hardware = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'