from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_agregado = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return f"Producto {self.id}: ({self.nombre})"