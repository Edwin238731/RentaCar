from django import forms
from .models import Auto

# Create your models here.

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'matricula', 'anio', 'precio_por_dia', 'disponible', 'estado']
