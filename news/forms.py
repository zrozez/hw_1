from django import forms
from django.forms import fields
from news.models import News

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'body', ]

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.TextInput(attrs={'class': 'form-control'})
    }