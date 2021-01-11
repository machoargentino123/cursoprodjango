from django import forms


from .models import Empleados

class EmpleadosForm(forms.ModelForm):
    """Form definition for Empleados."""

    class Meta:
        """Meta definition for Empleadosform."""

        model = Empleados
        fields = ('first_name',
                  'last_name',
                  'job',
                  'departamento',
                  'Avatar',
                  'habilidad',
                  'hoja_de_vida',      
         )
        #ojo con la s de widgets!!!!!!
        widgets = {
            'habilidad': forms.CheckboxSelectMultiple()
        }