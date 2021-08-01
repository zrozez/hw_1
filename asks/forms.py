from django import forms
from django.forms import fields
from asks.models import Ask

class AskForm(forms.ModelForm):

    class Meta:
        model = Ask
        fields = ['name', 'email', 'body']

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'}),
        }