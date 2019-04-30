from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Nivel (models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class Formacion_Academica(models.Model):
    nombre = models.CharField(max_length=100,blank=True, null=True)
    institucion = models.CharField(max_length=100,blank=True, null=True)
    abrebiacion = models.CharField(max_length=10, blank=True, null=True)
    nivel = models.ForeignKey(Nivel,on_delete=models.DO_NOTHING,default="1")
    def __str__(self):
        return self.nombre
class Teacher(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=100, blank=True, null=True)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    foto = models.FileField(upload_to="img/maestros/", blank=True, null=True)#barra despues
    formacion = models.ManyToManyField(Formacion_Academica,verbose_name=("Formacion Academica"),blank=True) 
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self): #Python 2 __unicode__
        return self.email

class Tag(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True,auto_now=False)
    actualizado = models.DateField(auto_now=True,auto_now_add=False)
    def __str__(self):
        return self.nombre

class New(models.Model):
    titulo = models.CharField(max_length=100,blank=True, null=True)

