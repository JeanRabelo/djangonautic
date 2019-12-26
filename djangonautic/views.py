from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage topzera')
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('about alguma coisa')
    return render(request, 'about.html')
