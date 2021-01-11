from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy


from django.views.generic.edit import FormView #para forms no genericas
from django.views.generic import ListView #vista generica
from .forms import NewDepartamentoForm
from applications.personas.models import Empleados#importo el modelo empleados
from .models import Departamento #importo el modelo departamento




class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/lista.html"
    context_object_name = 'departamentos'


########################################################################################    

class NewdepartamentoView(FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'   

    def form_valid(self, form):
        print('****************Estamos en el form valid************************')
        #capturo los datos del metodo POST en el form, desde la clase (self, form)
        nombre = form.cleaned_data['nombre']
        apellido =  form.cleaned_data['apellido']
        departamento =  form.cleaned_data['departamento']
        shortname =  form.cleaned_data['shortname']

        print(type(nombre))

        #instancia para modelo Departamento con este guardo en el modelo dto

        depa = Departamento(
            name = departamento,
            short_name = shortname
        )
        depa.save()  

        # Instancia para modelo empleado en este caso 
        #no es necesario hacer empleados.save() 

        Empleados.objects.create( # pylint: disable=no-member
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento =  depa,
        )
        return super(NewdepartamentoView,self).form_valid(form)
    