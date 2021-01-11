#FORMULARIOS EN DJANGO#

from django import forms
from .models import Prueba #debo declarar el modelo

#pesonalizar un formulario
#la tengo que declarar en el archivo vies. 
class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for form."""
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'titulo': forms.TextInput(attrs={'size': 12, 'Placeholder': 'Ingrese titulo'}),
            'subtitulo': forms.TextInput(attrs={'size': 10, 'Placeholder': 'Ingrese subtitulo'}),
            'cantidad': forms.TextInput(attrs={'size': 10, 'Placeholder': 'Ingrese Cantidad'}),
            
            
            }
        
    def clean_cantidad (self):
        cantidad = self.cleaned_data['cantidad']
            
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
            
        print(cantidad)
        return cantidad