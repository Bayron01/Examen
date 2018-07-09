from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.CharField(max_length=9, help_text="Ej: 962458090")
    direccion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='profesor')
    
	