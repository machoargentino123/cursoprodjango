from django.contrib import admin
from .models import Empleados, Habilidades
# Register your models here.



#esta clase me poermite indicar que campos se mostraran cuando abra al tabla en el admin.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','Area','job','full_name') #que campos mostrare en el admisnitrador
    search_fields = ('first_name',)
    list_filter = ('job','habilidad','departamento')
    #
    filter_horizontal = ('habilidad',)#solo funciona para cambpos muchos a muchos

    def full_name(self,object): #full name no existe en models debo crearlo
        print('----------------------')
        print(object.first_name) #muestro que es el objeto.
        print(object.first_name)
        print('----------------------')
        return object.first_name + ' ' + object.last_name 


    def Area(self, object):
        return object.departamento.short_name


admin.site.register(Empleados,EmpleadoAdmin)
admin.site.register(Habilidades)