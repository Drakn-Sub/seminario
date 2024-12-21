# seminario/models.py
from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADOS = [
        ('reservado', 'Reservado'),
        ('completada', 'Completada'),
        ('anulada', 'Anulada'),
        ('no_asisten', 'No Asisten'),
    ]
    
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True, null=True)
    cantidad_personas = models.PositiveIntegerField()
    institucion = models.ForeignKey(Institucion, related_name='inscritos', on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.nombre} ({self.institucion.nombre})"
