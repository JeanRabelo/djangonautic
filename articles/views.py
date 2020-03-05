from django.shortcuts import render, redirect
from .models import Artigo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    artigos = Artigo.objects.all()
    return render(request, 'articles/article_list.html', {'lista_de_artigos': artigos})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Artigo.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.author = request.user
            instancia.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()

    return render(request, 'articles/article_create.html', {'form': form})
