#Realizamos operaciones crud sobre el objeto
from rest_framework import viewsets

#importamos las clases 
from .models import Pacientes
from .serializer import PacientesSerializer

class PacientesViewSet(viewsets.ModelViewSet):
    #Definimos un atributo llamado queryset
    #Se trabajaran solo operaciones CRUD
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer