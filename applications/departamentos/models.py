from django.db import models

# Create your models here.
#nunca te olvides de indicar esta app en installed apps agregar app.


class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=100) #'nombre' es como aparecera en el administrador de django.
    short_name = models.CharField('Abreviatura del dto',max_length=20,unique=True)#con unique le decimos a django que nos e repitae en otros registros
    anulate = models.BooleanField('Anulado',default=False) #este campo no esta en el modelo del ejericio de ejemplo que vamos a usar.
    #decorador me permitira decorar lo que se vea en el adminsitrador de django.
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Areas departamentales'
        ordering = ['name'] #ordeno por orden alfabetico los registros
        unique_together = ['name','short_name'] # impido que se vuelva a repetir una combinacion de area y shortname

    def __str__(self):
        return str(self.id) + "-" + self.name + " - " + self.short_name # pylint: disable=no-member