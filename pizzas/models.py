from django.db import models

# Create your models here.
class Pizzas(models.Model):
    class Seccion(models.TextChoices):
        PIZZAS='PIZZAS','Pizzas'
        SPAGHETTIS='SPAGHETTIS','Spaghettis'
        ENTRANTES='ENTRANTES','Entrantes'
    seccion=models.CharField(max_length=30,choices=Seccion.choices,default=Seccion.PIZZAS)
    nombre=models.CharField(max_length=50)
    precio=models.TextField(default="1000 cup")
    foto=models.TextField(blank=True,default='')
 
def __str__(self):
    return self.nombre