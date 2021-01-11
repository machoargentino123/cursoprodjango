from django.db import models

# importo las vistas genericasd e django
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=30)
    cantidad = models.IntegerField()

    def __str__(self):
        resultado = str(self.id) + self.titulo + self.subtitulo + ' valor: ' +  str(self.cantidad)# pylint: disable=no-member
        return resultado