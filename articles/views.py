from django.shortcuts import render
from .models import Artigo

# Create your views here.
def article_list(request):
    artigos = Artigo.objects.all()
    return render(request, 'articles/article_list.html', {'lista_de_artigos': artigos})

def article_list0(request):
    artigos = Artigo.objects.all()
    return render(request, 'articles/article_list0.html', {'lista_de_artigos': artigos})

def lista_de_artigos(request):
    return render(request, 'articles/lista_de_artigos.html')
