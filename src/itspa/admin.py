from django.contrib import admin

from .models import Archivo, Proceso,Tag,Noticia

# Register your models here.

class AdminProceso(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle = Proceso

class AdminArchivo(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle = Archivo
class AdminNoticia(admin.ModelAdmin):
    list_display = ["titulo","timestamp"]

    class Meta:
        modle = Noticia
class AdminTag(admin.ModelAdmin):
    list_display=["nombre","timestamp"]

    class Meta:
        modle = Tag


admin.site.register(Proceso,AdminProceso)
admin.site.register(Archivo,AdminArchivo)
admin.site.register(Tag,AdminTag)
admin.site.register(Noticia,AdminNoticia)
