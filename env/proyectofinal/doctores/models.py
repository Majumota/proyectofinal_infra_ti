from django.db import models

# Create your models here.

class Doctores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.TextField()

    def __str__(nombre1):
        return nombre1.nombre
