from django.shortcuts import render

#impporto las vistas genericas
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  CreateView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)


#importo el modelo empleado
from .models import Empleados

#importo reverse_lazy
from django.urls import reverse_lazy

from .forms import EmpleadosForm

# Create your views here.
# 1- Listar Todos los empleados de la empresa.
# 2- Listar a todos los emplaedos que pertencen a un area de la empresa
# 3- Listar empleador por trabajo.
# 4- Listar los empleados por palabra clave
# 5- Listar habilidades de empleados.


### aca arranca el projecto propiamente dicho

##creamos la pagina home
##cvista que carga pa pagina de nincio

class InicioView(TemplateView):
    template_name = "inicio.html"



# 1- Listar Todos los empleados de la empresa.

class ListAllEmpleados(ListView):
    template_name = 'personas/list_all.html'
    paginate_by = 5 #para evitar sobrecargar el server me devuelve solo 2 registros. 
    #proba en la URL http://127.0.0.1:8000/listar_empleados/?page=3
    ordering = 'first_name'
    # model = Empleados # Si ejecutamos la funcion get_queryset no es necesario el model
    context_object_name = 'lista'

    def get_queryset(self): 
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleados.objects.filter( first_name__icontains = palabra_clave) # pylint: disable=no-member
        return lista
    
    def get_ordering(self):
        return self.ordering

# 2- Listar a todos los emplaedos que pertencen a un area de la empresa

class ListByAreaEmpleados(ListView):
    template_name = 'personas/list_area.html'
    context_object_name = 'empleados'
    #cuando tiene queryset no necesita el modelo.
    def get_queryset(self):
        filtro = self.kwargs['shorname']
        palabra_clave = self.request.GET.get('kword', '') #para cuadro buscar
            
        if palabra_clave != '':
            lista = Empleados.objects.filter(# pylint: disable=no-member
                last_name__icontains = palabra_clave
                ).filter(departamento__short_name=filtro)
            return lista
        else:
            lista = Empleados.objects.filter(# pylint: disable=no-member
                departamento__short_name=filtro)
            return lista


# 4- Listar los empleados por palabra clave
class EmpleadoDetailView2(DetailView):
    model = Empleados
    template_name = 'personas/detail_empleado2.html'  

    def get_context_data(self,**kwargs):# pylint: disable=no-member
        context = super(EmpleadoDetailView2, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes' #se crea la variable titulo para poner en el html
        #que tendra el valor empleado del mes
        return context

# 5 - pagina para listar empleados y administrarlos.

class AdminisitrarEmpleados(ListView):
    template_name = 'personas/admin_all.html'
    paginate_by = 10
    ordering = 'first_name'
    # model = Empleados # Si ejecutamos la funcion get_queryset no es necesario el model
    context_object_name = 'lista'
    model = Empleados

# 6- Editar empleado


class EmpleadoUpdateView(UpdateView): #necesita de un pk en el link de urls.py
    model = Empleados
    template_name = "personas/update.html"
    fields = ['first_name','last_name', 'job','departamento','habilidad']
    success_url = reverse_lazy('persona_app:administrar')

    #guarda depues de validar
    def form_valid(self,form):
        #logica de la funcion.
        return super(EmpleadoUpdateView,self).form_valid(form)



 # 7- Borrar un Empleado.   

class EmpleadoDeleteView(DeleteView):# pylint: disable=no-member
    #no se elimina por que si por lo que debo indicar si realmente se desea eliminar
    #para eso es el template.
    model = Empleados
    template_name = "personas/delete.html"
    success_url = reverse_lazy('persona_app:administrar')

# 8 - Agregar un empleado 

class AddEmpleados(CreateView):
    model = Empleados
    template_name = "personas/createview.html"
    #necesita un field 
    # fields = ('__all__')
    # o asignarle el form class
    form_class = EmpleadosForm
    success_url = reverse_lazy('persona_app:Empleados_all') #que derive a la pagina de todos los empleados
    
    def form_valid(self,form):
        #logica de la funcion.
        empleados = form.save(commit = False)
        empleados.full_name = empleados.first_name + ' ' + empleados.last_name
        empleados.save()
        return super(AddEmpleados,self).form_valid(form)


##############################Ejemplos todo lo de arriba es lo operativo########################################







 

#filtro + recomendado.  
class ListByJob(ListView):
    template_name = 'personas/list_area.html'
    model = Empleados
    def get_queryset(self):
        lista = Empleados.objects.filter( # pylint: disable=no-member
        job = '3'#modelo empleados columna job.
        )     
        return lista 


#filtro + varibale desde url.  revisar URL para ver como pasar la variable. 
class ListByURL(ListView):
    template_name = 'personas/list_area.html'
    model = Empleados
   
    def get_queryset(self):
        area = self.kwargs['shortname']  #variable se va llamar area 
        lista = Empleados.objects.filter( # pylint: disable=no-member

        departamento__short_name = area  #modelo empleados columna job.
        )     
       
        return lista


class ListByKeyword(ListView):
    template_name = 'personas/by_keyword.html'
    context_object_name = 'empleados' #como se va a llamar la variable en el html

    def get_queryset(self): 
        print("*************************************************")
        palabra_clave = self.request.GET.get('kword','')
        
        lista = Empleados.objects.filter( first_name = palabra_clave) # pylint: disable=no-member

        print(type(lista))
        print('Resultado',lista)

        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'personas/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        #habilidades es un many to many. Una habilidad pertenece a varios empleados y un empleado 
        #puede tener varias habilidades.
        empleado = Empleados.objects.get(id = 4)# pylint: disable=no-member
        print(empleado.habilidad.all()) 

        return empleado.habilidad.all()





#detailed view.
class EmpleadoDetailView(DetailView):
    model = Empleados
    template_name = 'personas/detail_empleado.html'



#create view necesita el template, el modelo, los campos a rellenar y una succes url que es
#a donde encara la pagina cuando se des submit al boton
class EmpleadoCreateView(CreateView):
    model = Empleados
    template_name = "personas/Createview.html"
    #necesita un field 
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:correcto') #uso la etiqueta name que le puse en urls


class SuccessCreateView(CreateView):
    model = Empleados
    template_name = "personas/success.html"
    #necesita un field 
    fields = ('__all__')
    success_url = "." #que deriv

class SuccessCreateView3(CreateView):
    model = Empleados
    template_name = "personas/success2.html"
    #necesita un field 
    fields = ('__all__')
    success_url = "." #que deriv

class EmpleadoCreateView2(CreateView):
    model = Empleados
    template_name = "personas/Createview.html"
    #necesita un field 
    fields = ['first_name','last_name', 'job','departamento','habilidad']
    success_url = reverse_lazy('persona_app:correcto2') #uso la etiqueta name que le puse en urls
    #def form_valid captura lo que se cargo validamente en el formulario
    def form_valid(self,form):
        #logica de la funcion.
        empleado = form.save() #guarde lo que se ingresado en el formulario
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name 
        empleado.save() #actualizo el full name
        return super(EmpleadoCreateView2,self).form_valid(form)


class SuccessCreateView2(CreateView):
    model = Empleados
    template_name = "personas/success.html"
    #necesita un field 
    fields = ['first_name','last_name', 'job','departamento','habilidad']
    success_url = "." #que derive a la misma pagina


#necesita de un pk en el link de urls.py
class EmpleadoUpdateView2(UpdateView): 
    model = Empleados
    template_name = "personas/update.html"
    fields = ['first_name','last_name', 'job','departamento','habilidad']
    

    #guarda depues de validar
    def form_valid(self,form):
        #logica de la funcion.
        print('#######################')
        print('##########METODO FORM VALID#############')
        print('#######################')
        return super(EmpleadoUpdateView2,self).form_valid(form)# pylint: disable=no-member

    #PARA GUARDAR DATOS ANTES DEL form VALID#
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('#######################')
        print('#####METODO POST ESTO ESTA EN EL CODIGO DESPUES DEL FORM VALID#####')
        print('#######################')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    success_url = reverse_lazy('persona_app:correcto3')





    

