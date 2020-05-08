from rest_framework import routers
from .views import EjemploViewSet

rutasEjemplo = routers.DefaultRouter()
rutasEjemplo.register(r'ejemplo', EjemploViewSet)