from django.contrib import admin

# Register your models here.
from .models import Teacher,Nivel,Formacion_Academica,Tag,Formacion_Academica,Noticia

class AdminTeacher(admin.ModelAdmin):
    list_display = ["name","timestamp"]
    class Meta:
        modle = Teacher

class AdminNivel(admin.ModelAdmin):
    list_display  = ["nombre"]
    class Meta:
        modle = Nivel
class AdminFormacionAcademica(admin.ModelAdmin):
    list_display = ["nombre","institucion"]
    class Meta:
        modle = Formacion_Academica
class AdminTag(admin.ModelAdmin):
    list_display =  ["nombre"]

    class Meta:
        modle = Tag
class AdminNoticia(admin.ModelAdmin):
    list_display = ["titulo","autor"]

    class Meta:
        modle = Noticia

admin.site.register(Teacher,AdminTeacher)
admin.site.register(Nivel,AdminNivel)
admin.site.register(Formacion_Academica,AdminFormacionAcademica)
admin.site.register(Tag,AdminTag)
admin.site.register(Noticia,AdminNoticia)