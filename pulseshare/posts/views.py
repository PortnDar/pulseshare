from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
    }
    return render(request, 'posts/home.html', context)


def group_posts(request, slug):
    context = {
    }
    return render(request, 'posts/group_list.html', context)
