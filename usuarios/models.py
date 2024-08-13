from django.db import models
from django.contrib.auth.models import User
#Images
from django_resized import ResizedImageField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)  

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)  
    descripcion = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0) 
    imagen = ResizedImageField(size = [600, 600], quality = 85,upload_to='productos/', blank=True, null=True)  

    def __str__(self):
        return self.nombre