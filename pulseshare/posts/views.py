from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def home(request):
    posts = Post.objects.select_related('author', 'group').all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/home.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    context = {
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)
