from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list),
    path('lista_de_artigos/', views.lista_de_artigos),
    path('0/', views.article_list0)
]
