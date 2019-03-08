from django.db import models

# Create your models here.
# Modelo para la tabla maestros
class Teacher(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    