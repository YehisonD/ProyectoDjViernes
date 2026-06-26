from django.db import models
from django.contrib.auth.models import User

class Componente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Registrado por')
    CATEGORIA_CHOICES = [
        ('CPU', 'CPU'),
        ('GPU', 'GPU'),
        ('RAM', 'RAM'),
        ('Storage', 'Storage'),
        ('PSU', 'PSU'),
        ('Motherboard', 'Motherboard'),
        ('Cooler', 'Cooler'),
        ('Case', 'Case'),
    ]

    GAMA_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]

    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, verbose_name='Categoría')
    especificacion = models.TextField(verbose_name='Especificación')
    gama = models.CharField(max_length=10, choices=GAMA_CHOICES, default='media', verbose_name='Gama')
    precio = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) — ${self.precio}"
