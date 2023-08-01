from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

# Funcion inicio
def index(request):
    return render(request, "aplicacion/base.html")

# Funcion medicos
def medicos(request):
    ctx = {"medicos": Medico.objects.all() }
    return render(request, "aplicacion/medicos.html", ctx)

# Funcion pacientes
def pacientes(request):
    ctx = {"pacientes": Paciente.objects.all() }
    return render(request, "aplicacion/pacientes.html", ctx)

# Funcion historial clinico
def historialClinico(request):
    ctx = {"historial": HistorialClinico.objects.all() }
    return render(request, "aplicacion/historialClinico.html", ctx)

# Funcion hospital
def hospital(request):
    ctx = {"hospital": Hospital.objects.all() }
    return render(request, "aplicacion/hospital.html", ctx)

#____________________________

# Funcion formulario de medico
def medicoForm(request):
    if request.method == "POST":
        medico = Medico(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                        email=request.POST['email'], profesion=request.POST['profesion'])
        medico.save()
        return HttpResponse("Se guardo de manera correcta el Medico")
    return render(request, "aplicacion/medicoForm.html")

# Funcion main formulario de medico 
def medicoForm1(request):
    if request.method == "POST":
        miForm = MedicoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            medico = Medico(nombre=informacion['nombre'], apellido=informacion['apellido'],
                            email=informacion['email'], profesion=informacion['profesion'])
            medico.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = MedicoForm()

    return render(request, "aplicacion/medicoForm1.html", {"form":miForm}) 

# Funcion formulario de paciente
def pacienteForm1(request):
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            paciente= Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'],
                            email=informacion['email']) 
            paciente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = PacienteForm()
        
    return render(request, "aplicacion/pacienteForm1.html", {"form":miForm}) 

# Funcion formulario de hospital
def hospitalForm1(request):
    if request.method == "POST":
        miForm = HospitalForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            hospital= Hospital(nombre=informacion['nombre'], direccion=informacion['direccion'])             
            hospital.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = HospitalForm()
        
    return render(request, "aplicacion/hospitalForm1.html", {"form":miForm}) 

# Funcion formulario de Historial clinico
def historialForm1(request):
    if request.method == "POST":
        miForm = HistorialForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            historial= HistorialClinico(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                        fecha_nacimiento=informacion['fecha_nacimiento'],
                                          contacto_emergencia=informacion['contacto_emergencia'])             
            historial.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = HistorialForm()
        
    return render(request, "aplicacion/historialForm1.html", {"form":miForm}) 

# Funcion formulario para buscar en la base de datos
def buscarMedico(request):
    return render(request, "aplicacion/buscarMedico.html")

# Funcion que muestra lo buscado en el formulario
def buscar2(request):
    nombre = request.GET.get('nombre', '')  # Obtiene el parámetro 'nombre' o una cadena vacía si no está presente
    if nombre:
        medicos = Medico.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadosMedico.html", {"medicos": medicos, "nombre": nombre})
    return HttpResponse("No se ingresaron datos a buscar")
