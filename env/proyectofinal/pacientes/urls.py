from rest_framework import routers

from .viewsets import PacientesViewSet

#Define las rutas del modelo (Get,Post, Put) - API REST
router = routers.SimpleRouter() 
router.register('pacientes', PacientesViewSet)

urlpatterns = router.urls