from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def user_main(request):
    u = User.objects.all()
    print(u)
    return HttpResponse('Это страница, где ебется юзер')