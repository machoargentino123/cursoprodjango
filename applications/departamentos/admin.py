from django.contrib import admin
from .models import Departamento 

#aca debemos declarar la base de datos para poder administrarla desde el panel # 
#administrdor de django#
admin.site.register(Departamento)
