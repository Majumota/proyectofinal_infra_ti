from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroDocumento = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
