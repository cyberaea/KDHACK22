from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главное страница, где будет авторизация')