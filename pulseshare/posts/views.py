from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse('Список мороженого')
