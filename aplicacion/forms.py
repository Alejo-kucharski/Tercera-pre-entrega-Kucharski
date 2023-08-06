from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

# Form de medico
class MedicoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=40, required=True)
    apellido = forms.CharField(label="Apellido", max_length=40, required=True) 
    email = forms.EmailField(label="Email", max_length=50, required=False) 
    profesion = forms.CharField(label="Profesion", max_length=40, required=True)  

# Form de paciente
class PacienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=40, required=True)
    apellido = forms.CharField(label="Apellido", max_length=40, required=True) 
    email = forms.EmailField(label="Email", max_length=50, required=False) 

# Form de Hospital    
class HospitalForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=40, required=True)
    direccion = forms.CharField(label="Direccion", max_length=40, required=False)
    
# Form de Historial Clinico
class HistorialForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=40, required=True)
    apellido = forms.CharField(label="Apellido", max_length=40, required=True) 
    fecha_nacimiento = forms.DateField()
    contacto_emergencia = forms.IntegerField()  

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    

class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre/s", max_length=40, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=40, required=True) 
    email = forms.EmailField(label="Modifique su Email", max_length=50, required=False) 
    password1 = forms.CharField(label="Ingresar contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Ingrese nuevamente su contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
