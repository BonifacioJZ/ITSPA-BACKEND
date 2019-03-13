from django.contrib import admin

# Register your models here.
from .models import Teacher
class AdminTeacher(admin.ModelAdmin):
    list_display = ["__str__","nombre","timestamp"]
    class Meta:
        modle = Teacher
admin.site.register(Teacher,AdminTeacher)