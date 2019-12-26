from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    hora = models.TimeField(auto_now_add = True)

    def __str__(self):
        return self.titulo
