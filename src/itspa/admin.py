from django.contrib import admin

from .models import Archivo, Proceso

# Register your models here.

class AdminProceso(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle = Proceso

class AdminArchivo(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle = Archivo

admin.site.register(Proceso,AdminProceso)
admin.site.register(Archivo,AdminArchivo)
