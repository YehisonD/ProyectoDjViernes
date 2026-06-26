from django.contrib import admin
from .models import Componente


@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'gama', 'precio', 'stock', 'activo', 'created_at')
    list_filter = ('categoria', 'gama', 'activo')
    search_fields = ('nombre', 'especificacion')
    ordering = ('-created_at',)
