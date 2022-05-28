#Realizamos operaciones crud sobre el objeto
from rest_framework import viewsets

from .models import Doctores
from .serializer import DoctoresSerializer

class DoctoresViewSet(viewsets.ModelViewSet):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer
