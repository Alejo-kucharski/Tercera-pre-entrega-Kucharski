from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo medico
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.email}, {self.profesion}"

# Modelo Paciente    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.email}"

# Modelo Historial Clinico   
class HistorialClinico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    contacto_emergencia = models.IntegerField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.fecha_nacimiento}, {self.contacto_emergencia}"

# Modelo Hospital   
class Hospital(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.direccion}, {self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"
        