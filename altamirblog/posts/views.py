from django.shortcuts import render

posts = [
    {
    "id": 1,
    "titulo": "Titulo 1",
    "subtitulo": "Subtitulo 1",
    "descricao": "Descricao 1"
    },
    {
    "id": 2, 
    "titulo": "Titulo 2",
    "subtitulo": "Subtitulo 2",
    "descricao": "Descricao 2"
    },
    {
    "id": 3,   
    "titulo": "Titulo 3",
    "subtitulo": "Subtitulo 3",
    "descricao": "Descricao 3"
    },
    {
    "id": 4,
    "titulo": "Titulo 4",
    "subtitulo": "Subtitulo 4",
    "descricao": "Descricao 4"
    },
]

categorias = [
    
    "A","B","C","D"
    
]

def listar_posts(request):
    contexto = {
        'posts': posts
    }

    return render(request,"index.html", contexto)


def categorias_blogs(request):
    contexto = {
        'categorias': categorias
    }
    return render(request,"categorias.html", contexto)

def detalhar_post(request, id):
    post = posts[id-1]
    return render(request, "detalhar_post.html", {
        'post': post

    })