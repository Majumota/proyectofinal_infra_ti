from django.contrib import admin
from .models import Pacientes

# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','numeroDocumento')

admin.site.register(Pacientes,PacientesAdmin)