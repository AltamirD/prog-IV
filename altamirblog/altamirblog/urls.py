from django.contrib import admin
from django.urls import path
from posts.views import listar_posts, detalhar_post
from posts.views import categorias_blogs


urlpatterns = [
    path('posts/', listar_posts),
    path('categorias/', categorias_blogs),
    path('posts/<int:id>/', detalhar_post, name="post_detail")
]
