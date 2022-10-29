from django.shortcuts import render
from django.http import HttpResponse


def admin_main(request):
    return HttpResponse('Это страница, где ебется админ')