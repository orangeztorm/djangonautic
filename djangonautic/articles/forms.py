from django import forms

from . import models


class createArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body', 'thumb']
