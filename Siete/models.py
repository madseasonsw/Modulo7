from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Prioridad(models.Model):
    nombre = models.CharField(max_length=200)
    orden = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, related_name='usuario_creador', on_delete=models.CASCADE)
    usuario_asignado = models.ForeignKey(User, related_name='usuario_asignado', null=True, blank=True, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    observaciones = models.TextField(blank=True, null=True)
    observacion = models.TextField(null=True, blank=True)
    prioridad = models.ForeignKey(Prioridad, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre



