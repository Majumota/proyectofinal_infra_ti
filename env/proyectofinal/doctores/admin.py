from django.contrib import admin
from .models import Doctores

# Register your models here.

class DoctoresAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','especialidad')

admin.site.register(Doctores,DoctoresAdmin)