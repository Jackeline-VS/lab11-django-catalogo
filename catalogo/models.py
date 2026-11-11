from django.db import models

class Producto(models.Model):
    CATEGORIAS = [
        ('laptops', 'Laptops'),
        ('celulares', 'Celulares'),
        ('accesorios', 'Accesorios'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - S/ {self.precio}"