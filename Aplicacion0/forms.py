#este archivo es nuevo y su programación
from django import forms
#from .models import *

class RegForm(forms.Form):
        nombre=forms.CharField(label="Nombre",max_length=100)
        edad = forms.IntegerField(label="Edad")
