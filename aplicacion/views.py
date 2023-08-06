from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Class-Based-View Imports
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Authentication Imports
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

# Funcion inicio
def index(request):
    return render(request, "aplicacion/base.html")

# Funcion medicos
@login_required
def medicos(request):
    ctx = {"medicos": Medico.objects.all() }
    return render(request, "aplicacion/medicos.html", ctx)

# Funcion pacientes
@login_required
def pacientes(request):
    ctx = {"pacientes": Paciente.objects.all() }
    return render(request, "aplicacion/pacientes.html", ctx)

# Funcion historial clinico
@login_required
def historialClinico(request):
    ctx = {"historial": HistorialClinico.objects.all() }
    return render(request, "aplicacion/historialClinico.html", ctx)

# Funcion hospital
@login_required
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
@login_required 
def medicoForm1(request):
    if request.method == "POST":
        miForm = MedicoForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            medico = Medico(nombre=informacion['nombre'], apellido=informacion['apellido'],
                            email=informacion['email'], profesion=informacion['profesion'])
            medico.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = MedicoForm()

    return render(request, "aplicacion/medicoForm1.html", {"form":miForm}) 

# Funcion formulario de paciente
@login_required
def pacienteForm1(request):
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            paciente= Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'],
                            email=informacion['email']) 
            paciente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = PacienteForm()
        
    return render(request, "aplicacion/pacienteForm1.html", {"form":miForm}) 

# Funcion formulario de hospital
@login_required
def hospitalForm1(request):
    if request.method == "POST":
        miForm = HospitalForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            hospital= Hospital(nombre=informacion['nombre'], direccion=informacion['direccion'])             
            hospital.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = HospitalForm()
        
    return render(request, "aplicacion/hospitalForm1.html", {"form":miForm}) 

# Funcion formulario de Historial clinico
@login_required
def historialForm1(request):
    if request.method == "POST":
        miForm = HistorialForm(request.POST)
        print(miForm)
        if miForm.is_valid():
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
@login_required
def buscarMedico(request):
    return render(request, "aplicacion/buscarMedico.html")

# Funcion que muestra lo buscado en el formulario
@login_required
def buscar2(request):
    nombre = request.GET.get('nombre', '')  # Obtiene el parámetro 'nombre' o una cadena vacía si no está presente
    if nombre:
        medicos = Medico.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadosMedico.html", {"medicos": medicos, "nombre": nombre})
    return HttpResponse("No se ingresaron datos a buscar")


# Funciones de Update
@login_required
def updateMedico(request, id_medico):
    medico = Medico.objects.get(id=id_medico)
    if request.method == "POST":
        miForm = MedicoForm(request.POST)
        if miForm.is_valid():
            medico.nombre = miForm.cleaned_data.get('nombre')
            medico.apellido = miForm.cleaned_data.get('apellido')
            medico.email = miForm.cleaned_data.get('email')
            medico.profesion = miForm.cleaned_data.get('profesion')
            medico.save()
            return redirect(reverse_lazy('medicos')) # Redirecciona a la url'Medicos'
    else: 
        miForm = MedicoForm(initial={'nombre':medico.nombre,
                                     'apellido': medico.apellido,
                                     'email': medico.email,
                                     'profesion': medico.profesion}) 
    return render(request, "aplicacion/medicoForm1.html", {'form': miForm}) 

@login_required
def deleteMedico(request, id_medico):
    medico = Medico.objects.get(id=id_medico)
    medico.delete()
    return redirect(reverse_lazy('medicos'))

@login_required
def createMedico(request):
    if request.method == "POST":
        miForm = MedicoForm(request.POST)
        if miForm.is_valid():
            medico_nombre = miForm.cleaned_data.get('nombre')
            medico_apellido = miForm.cleaned_data.get('apellido')
            medico_email = miForm.cleaned_data.get('email')
            medico_profesion = miForm.cleaned_data.get('profesion')
            medico = Medico(nombre=medico_nombre,
                            apellido=medico_apellido, 
                            email=medico_email, 
                            profesion=medico_profesion)
            medico.save()
            return redirect(reverse_lazy('medicos'))
    else:
        miForm = MedicoForm()

    return render(request, "aplicacion/medicoForm1.html", {'form': miForm})

# Class Based View

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('pacientes')

class PacienteDetail(LoginRequiredMixin, DetailView):
    model = Paciente

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('pacientes')

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('pacientes')


# Logins, Logouts, Register

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, "mensaje": f"Ingresaste datos incorrectos"})
        else:  
            return render(request, "aplicacion/login.html", {'form': miForm, "mensaje": f"Ingresaste datos incorrectos"})           

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {'form': miForm})


def register(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(request.POST) 
        if miForm.is_valid():  
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        miForm = RegistroUsuariosForm() 

    return render(request, "aplicacion/registro.html", {"form": miForm})   


# Registracion usuarios
@login_required
def perfilEdit(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            usuario.email = miForm.cleaned_data('email')
            usuario.password1 = miForm.cleaned_data('password1')
            usuario.password2 = miForm.cleaned_data('password2')
            usuario.first_name = miForm.cleaned_data('first_name')
            usuario.last_name = miForm.cleaned_data('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {"mensaje": f"El usuario {usuario.username} se ha actualizado de manera correcta!"})
        else:
            return render(request, "aplicacion/editarForm.html", {"form": miForm})
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editUser.html", {"form": miForm, "usuario": usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarFormulario(request.POST, request.FILES)
        if miForm.is_valid():
            u = User.objects.get(username=request.user)
            #__ Eliminacion del Avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si es mayor a 0 significa que ya hay un avatar
                avatarViejo[0].delete()

            #__ Creacion del nuevo Avatar
            avatar = Avatar(user=u, imagen=miForm.cleaned_data['imagen'])
            avatar.save()

            #__ Almacenamiento del nuevo avatar
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        miForm = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm})
