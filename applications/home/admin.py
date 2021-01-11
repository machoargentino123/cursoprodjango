from django.contrib import admin
from .models import Prueba
# Register your models here.
#aca debemos declarar la base de datos para poder administrarla desde el panel # 
#administrdor de django#
admin.site.register(Prueba)
#admin.site.register(Departamento)