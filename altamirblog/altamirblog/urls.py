from django.contrib import admin
from django.urls import path
from posts.views import listar_posts, detalhar_post
from posts.views import categorias_blogs
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('posts/', listar_posts),
    path('categorias/', categorias_blogs),
    path('posts/<int:id>/', detalhar_post, name="post_detail")
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
