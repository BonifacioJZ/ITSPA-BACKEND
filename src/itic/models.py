from django.db import models

# Create your models here.

class Teacher(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=100, blank=True, null=True)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    foto = models.FileField(upload_to="img/maestros/", blank=True, null=True)#barra despues 
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self): #Python 2 __unicode__
        return self.email
class Proceso(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    notas = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)

class Archivo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to="files/")
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)
    
