from django import forms

from .models import Departamento



class NewDepartamentoForm(forms.Form):
    """Form definition for NewDepartamento."""
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=20)