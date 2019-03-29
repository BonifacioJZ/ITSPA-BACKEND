from django.contrib import admin

# Register your models here.
from .models import Teacher
from .models import Proceso
from .models import Archivo
class AdminTeacher(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle = Teacher
class AdminProcesos(admin.ModelAdmin):
    list_display = ["nombre","timestamp"]
    class Meta:
        modle= Proceso
class AdminArchivos (admin.ModelAdmin):

    list_display = ["nombre","timestamp"]
    class Meta:
        modle= Archivo

admin.site.register(Teacher,AdminTeacher)
admin.site.register(Proceso,AdminProcesos)
admin.site.register(Archivo,AdminArchivos)