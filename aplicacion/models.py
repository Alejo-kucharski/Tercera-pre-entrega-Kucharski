from django.db import models

# Create your models here.

# Modelo medico
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# Modelo Paciente    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# Modelo Historial Clinico   
class HistorialClinico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    contacto_emergencia = models.IntegerField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# Modelo Hospital   
class Hospital(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.direccion}, {self.nombre}"