from django.db import models
from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    date_of_birthday = forms.CharField(max_length=100, required=True)
    
    
    
    