from django.db import models

# Create your models here.

class Libro(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial =models.CharField(max_length=30)
    calificacion = models.PositiveIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.calificacion)