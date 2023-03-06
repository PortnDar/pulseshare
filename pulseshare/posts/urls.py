from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
