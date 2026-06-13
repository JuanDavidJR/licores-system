from django.shortcuts import render
from .models import Venta

def ventas_lista(request):
    ventas = Venta.objects.all().order_by('-fecha')
    total_dia = sum(v.total for v in ventas)
    return render(request, 'ventas/ventas.html', {
        'ventas': ventas,
        'total_dia': total_dia,
    })