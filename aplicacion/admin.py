from django.contrib import admin
from .models import *


# Register your models here.

# Dar de Alta los Models
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Hospital)
admin.site.register(HistorialClinico)

