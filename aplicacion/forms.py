from django import forms

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

