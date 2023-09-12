from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__ (self) -> str:
        return f'{self.titulo} <-> {self.subtitulo} <-> {self.descricao} '