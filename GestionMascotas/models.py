from django.db import models

# Create your models here.
class Mascota(models.Model):
    codigo = models.CharField(max_length=10)
    nombre =  models.CharField(max_length=30)
    talla = (('XS', 'Extra pequeño'), ('S', 'Pequeño'), ('M', 'Mediano'), ('L', 'Grande'), ('XL', 'Extra grande'))
    tamano = models.CharField(max_length=2, choices=talla, default='M')
    peso = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    fechaRescate = models.DateField()
    estados = (('Disponible', 'Disponible'), ('Rescatado', 'Rescatado'), ('Adoptado', 'Adoptado'))
    estado = models.CharField(max_length=10, choices=estados, default='Rescatado')

    def __str__(self):
        return self.nombre