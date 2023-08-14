from django.shortcuts import render

posts = [
    {
    "titulo": "Titulo 1",
    "subtitulo": "Subtitulo 1",
    "descricao": "Descricao 1"
    },
    {
    "titulo": "Titulo 2",
    "subtitulo": "Subtitulo 2",
    "descricao": "Descricao 2"
    },
    {
    "titulo": "Titulo 3",
    "subtitulo": "Subtitulo 3",
    "descricao": "Descricao 3"
    },
    {
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

