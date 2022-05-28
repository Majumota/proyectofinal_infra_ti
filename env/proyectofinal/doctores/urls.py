from rest_framework import routers

from .viewsets import DoctoresViewSet

#Define las rutas del modelo (Get,Post, Put) - API REST
router = routers.SimpleRouter() 
router.register('doctores', DoctoresViewSet)

urlpatterns = router.urls


