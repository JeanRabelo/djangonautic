from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Artigo
        fields = ['titulo', 'slug', 'body', 'thumb']
