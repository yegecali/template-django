from .serializers import EjemploSerializers
from rest_framework import viewsets
from ..models import Ejemplo
class EjemploViewSet(viewsets.ModelViewSet):
    queryset = Ejemplo.objects.all()
    serializer_class = EjemploSerializers