# PERMITE SERIALIZAR EL MODELO MEDIANTE PROTOCOLO HTTP
from .models import Doctores
from rest_framework import serializers

#Generamos nueva clase la cual hereda de model serializer
class DoctoresSerializer(serializers.ModelSerializer):
   # Definimos la clase meta para definir el modelo y campos a trabajar
   class Meta:
        model = Doctores 
        fields='__all__'