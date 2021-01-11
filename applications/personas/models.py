from django.db import models
from applications.departamentos.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=100)

    class Meta:
            verbose_name = 'Habilidad'
            verbose_name_plural = 'Habilidades de los Empleados'
    def __str__(self):
        return str(self.id) + '-' + self.habilidad# pylint: disable=no-member

class Empleados(models.Model):
    '''Modelo para tabla empleado'''
    TRABAJOS = (('0','CONTADOR'),('1','ADMINISTRATIVO'),('2','ECONOMISTA'),('3','OTRO')) #opciones para job


    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellido',max_length=60)
    full_name = models.CharField('Nombre completo', max_length=120,blank=True)
    job = models.CharField('Puesto',max_length=30,choices=TRABAJOS)
    #Departamento lo voy a importar del modelo Departamento.
    # En este caso la reclacion que hace es de 1 a muchos.
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Avatar = models.ImageField('Foto',upload_to='media/empleado', blank = True, null=True)
    habilidad = models.ManyToManyField(Habilidades) #relacion de muchos a muchos
    hoja_de_vida = RichTextField()#agrego una ventana  para agregar texto con formato. libreria ckeditor
    class Meta:
            verbose_name = 'Empleado'
            verbose_name_plural = 'Empleados'
            

  #  def __str__(self):
  #      trabajo = str(self.job)   
  #      print(trabajo) 
  #      return str(self.id) + ' ' + self.first_name + ' ' + self.last_name + ' ' + trabajo + ' ' + str(self.departamento)# pylint: disable=no-member