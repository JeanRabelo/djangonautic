from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    hora = models.TimeField(auto_now_add = True)
    thumb = models.ImageField(default='logo-default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

    def snippet(self):
        if len(self.body)<51:
            return self.body
        else:
            return self.body[:50] + ' (...)'
