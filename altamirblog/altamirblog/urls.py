from django.contrib import admin
from django.urls import path
from posts.views import listar_posts
from posts.views import categorias_blogs

urlpatterns = [
    path('', listar_posts),
    path('categorias/', categorias_blogs)
]
