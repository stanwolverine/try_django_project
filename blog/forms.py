from django import forms
from .models import Article


class ArticleCreateForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField()
    active = forms.BooleanField()
