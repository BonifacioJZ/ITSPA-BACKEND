from django.db import models
from tinymce.models import HTMLField
# Create your models here.


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
    descripcion = HTMLField()
    color = models.CharField(max_length=15,blank=True, null=True)
    archivos= models.IntegerField(choices=ESTADOS,default=2,verbose_name=("Contiene Archivos"))
    tipo_proceso= models.IntegerField(choices=TIPO,default=1,verbose_name=("Tipo de Proceos"))
    archivo_proceso = models.ManyToManyField(Archivo, verbose_name=("archivos"),blank=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    actualizado = models.DateField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.nombre
    
