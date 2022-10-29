from django.shortcuts import render
from django.http import HttpResponse


def user_main(request):
    return HttpResponse('Это страница, где ебется юзер')