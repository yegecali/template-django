from ..models import Ejemplo
from rest_framework import serializers

class EjemploSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ejemplo
        fields = ('nombre')