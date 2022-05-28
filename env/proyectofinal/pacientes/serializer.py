# PERMITE SERIALIZAR EL MODELO MEDIANTE PROTOCOLO HTTP
from .models import Pacientes
from rest_framework import serializers

#Generamos nueva clase la cual hereda de model serializer
class PacientesSerializer(serializers.ModelSerializer):
   # Definimos la clase meta para definir el modelo y campos a trabajar
   class Meta:
        model = Pacientes 
        fields='__all__'