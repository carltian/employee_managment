
__author__ = 'carl'
from django import forms
class ContentForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.IntegerField(max_value= 20)