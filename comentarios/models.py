from django.db import models
from django.utils import timezone
class Comentarios(models.Model):
    nombre_persona=models.CharField(max_length=20,default="Juan")
    nombre_oferta=models.CharField(max_length=20,default='Pizza de Queso')
    numero_oferta=models.IntegerField(default=1)
    comentario=models.TextField()
    resumen=models.CharField(max_length=23,default='Exquisito')
    gradoSatisfaccion=models.TextField(default="Bien")
    fecha = models.DateTimeField(default=timezone.now)
"""     calificacion=models.CharField(max_length=90,default="Sin calificar",blank=True) """
def __str__(self):
    return self.resumen    