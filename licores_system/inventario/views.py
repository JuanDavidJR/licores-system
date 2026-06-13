from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def inventario_lista(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/inventario.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        stock_minimo = request.POST.get('stock_minimo')
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock=stock,
            stock_minimo=stock_minimo
        )
    return redirect('inventario')

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.stock_minimo = request.POST.get('stock_minimo')
        producto.save()
    return redirect('inventario')

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('inventario')