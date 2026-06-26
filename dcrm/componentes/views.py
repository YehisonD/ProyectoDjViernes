from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Componente
from .forms import ComponenteForm


@login_required
def componentes_list(request):
    """Listar componentes con filtros (equivalente a GET del API PHP)."""
    qs = Componente.objects.all()

    # Filtro búsqueda
    buscar = request.GET.get('buscar', '').strip()
    if buscar:
        qs = qs.filter(
            Q(nombre__icontains=buscar) | Q(especificacion__icontains=buscar)
        )

    # Filtro categoría
    categoria = request.GET.get('categoria', '')
    if categoria:
        qs = qs.filter(categoria=categoria)

    # Filtro estado activo
    activo = request.GET.get('activo', '')
    if activo == '1':
        qs = qs.filter(activo=True)
    elif activo == '0':
        qs = qs.filter(activo=False)

    # Filtro precio mínimo
    precio_min = request.GET.get('precio_min', '')
    if precio_min:
        try:
            qs = qs.filter(precio__gte=float(precio_min))
        except ValueError:
            pass

    # Filtro precio máximo
    precio_max = request.GET.get('precio_max', '')
    if precio_max:
        try:
            qs = qs.filter(precio__lte=float(precio_max))
        except ValueError:
            pass

    # Filtro solo con stock
    con_stock = request.GET.get('con_stock', '')
    if con_stock == '1':
        qs = qs.filter(stock__gt=0)

    # Filtro mis componentes
    mis_componentes = request.GET.get('mis_componentes', '')
    if mis_componentes == '1':
        qs = qs.filter(usuario=request.user)

    # Stats
    total = Componente.objects.count()
    activos = Componente.objects.filter(activo=True).count()
    inactivos = Componente.objects.filter(activo=False).count()
    con_stock_count = Componente.objects.filter(stock__gt=0).count()

    context = {
        'componentes': qs,
        'categorias': Componente.CATEGORIA_CHOICES,
        'filtros': {
            'buscar': buscar,
            'categoria': categoria,
            'activo': activo,
            'precio_min': precio_min,
            'precio_max': precio_max,
            'con_stock': con_stock,
            'mis_componentes': mis_componentes,
        },
        'stats': {
            'total': total,
            'activos': activos,
            'inactivos': inactivos,
            'con_stock': con_stock_count,
        }
    }
    return render(request, 'componentes_list.html', context)


@login_required
def componente_create(request):
    """Crear un nuevo componente (equivalente a POST del API PHP)."""
    if request.method == 'POST':
        form = ComponenteForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.usuario = request.user
            comp.save()
            messages.success(request, "Componente registrado correctamente")
            return redirect('componentes_list')
    else:
        form = ComponenteForm()
    return render(request, 'componente_create.html', {'form': form})


@login_required
def componente_delete(request, pk):
    """Eliminación lógica — desactivar componente (equivalente a DELETE del API PHP)."""
    comp = get_object_or_404(Componente, pk=pk)

    if not comp.activo:
        messages.warning(request, "El componente ya está inactivo")
        return redirect('componentes_list')

    if comp.stock > 0:
        messages.error(
            request,
            f'No se puede eliminar: tiene {comp.stock} unidad(es) en inventario. Primero reduce el stock a 0.'
        )
        return redirect('componentes_list')

    comp.activo = False
    comp.save()
    messages.success(request, f'Componente "{comp.nombre}" eliminado correctamente')
    return redirect('componentes_list')


@login_required
def componente_reactivar(request, pk):
    """Reactivar componente (equivalente a PATCH del API PHP)."""
    comp = get_object_or_404(Componente, pk=pk)

    if comp.activo:
        messages.warning(request, "El componente ya está activo")
        return redirect('componentes_list')

    comp.activo = True
    comp.save()
    messages.success(request, f'Componente "{comp.nombre}" reactivado correctamente')
    return redirect('componentes_list')
