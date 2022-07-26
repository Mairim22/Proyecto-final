#from mailbox import NoSuchMailboxError
import email
from email.mime import image
from mailbox import NoSuchMailboxError
from pickle import TRUE
from django.db import models
from django.forms import DateTimeField, EmailField
from django.contrib.auth.models import User
from distutils.command.upload import upload

# Create your models here.

class Clases(models.Model):
    nombre= models.CharField(max_length=30)
    horario= models.TimeField (max_length=30)
    descripcion = models.CharField(max_length=100)
    def __str__(self):return f"Nombre: {self.nombre} - Horario {self.horario} - Descripcion {self.descripcion}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, null=True)
    texto = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre



class Img(models.Model):
    img = models.ImageField()


