from django.contrib import admin

# Register your models here.
from reporte.models import Persona,Vacuna,Vacunacion
admin.site.register(Persona)
admin.site.register(Vacuna)
admin.site.register(Vacunacion)
