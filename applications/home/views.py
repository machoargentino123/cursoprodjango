from django.shortcuts import render
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  CreateView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)

from .models import Prueba
# Create your views here.
from .forms import PruebaForm
import datetime
class PruebaView(TemplateView):
    template_name = "home/prueba.html"


class ResumenfoundationView(TemplateView):
    template_name = "home/resumenfoundation.html"
    #### sOLO ME PERMITE UNSAR UN get NADA MAS SI CREO UN TERCENO ENTRARA EN EL ULtIMO

    def get(self, request, *args, **kwargs):
        fecha = datetime.datetime.now()
        context = {'fecha': fecha}
        print("********entro en fecha**************")
        return self.render_to_response(context)
    def get(self, request, *args, **kwargs):
        print("********entro en posicion**************")
        posicion = 2+2 
        context = {'posicion': posicion}
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        print("********entro en posicion2**************")
        posicion = 2+2+2*3 
        context = {'posicion2': posicion}
        return self.render_to_response(context)



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listanumeros'
    queryset = ['1','2','30','40','25','1569']
    
class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm #matchea a el archivo form para poder modificar los forms de los genericviews
    success_url = '/'



    