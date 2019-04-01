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

class Archivo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    archivo = models.FileField(upload_to="files/", blank=True, null=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.nombre
        
class Proceso(models.Model):
    ESTADOS = ((1,"Si"),(2,"No"))
    TIPO =((1,"Residencias"),(2,"Servicio"))
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    archivos= models.IntegerField(choices=ESTADOS,default=2,verbose_name=("Contiene Archivos"))
    tipo_proceso= models.IntegerField(choices=TIPO,default=1,verbose_name=("Tipo de Proceos"))
    archivo_proceso = models.ManyToManyField(Archivo, verbose_name=("archivos"),blank=True)
    notas = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.nombre
    
