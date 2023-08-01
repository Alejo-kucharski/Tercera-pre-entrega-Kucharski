from django.urls import path
from .views import *

urlpatterns = [
    # Funcion de inicio
    path('inicio', index, name="inicio"),

    # Funciones de los models
    path('medicos/', medicos, name="medicos"),
    path('pacientes/', pacientes, name="pacientes"),
    path('hostorialClinico', historialClinico, name="historial_clinico"),
    path('hospital/', hospital, name="hospital"),

    #
        # Funciones de los forms
        path('medico_Form/', medicoForm, name="medicoform"),
        path('medico_Form1/', medicoForm1, name="medicoform1"),
        path('paciente_Form1/', pacienteForm1, name="pacienteform1"),
        path('hospital_Form1/', hospitalForm1, name="hospitalform1"),
        path('historial_Form1/', historialForm1, name="historialform1"),
    #
        # Funciones de los forms de busqueda
        path('buscar_medico/', buscarMedico, name="buscar_medico"),
        path('buscar2/', buscar2, name="buscar2"),

]