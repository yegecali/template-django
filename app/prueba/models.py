from django.db import models

# Create your models here.
class Ejemplo(models.Model):
    id_ejemplo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)