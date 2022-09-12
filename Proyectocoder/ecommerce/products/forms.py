from socket import fromshare
from django import forms

class Formulario_productos(forms.Form):
    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    stock=forms.IntegerField()
    image=forms.ImageField(required=False)
