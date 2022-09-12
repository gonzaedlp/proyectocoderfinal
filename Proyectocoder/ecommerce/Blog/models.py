from django.db import models

# Create your models here.
class Articles(models.Model):
    titulo=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=500)
    autor=models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True, blank=True, null=True)

class Personal(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    puesto = models.CharField(max_length=40)
