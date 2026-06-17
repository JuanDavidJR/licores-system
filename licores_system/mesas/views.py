from django.shortcuts import render, get_object_or_404, redirect
from .models import Mesa, Pedido, DetallePedido
from inventario.models import Producto

def mesas_lista(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        if numero and not Mesa.objects.filter(numero=numero).exists():
            Mesa.objects.create(numero=numero)
    mesas = Mesa.objects.all().order_by('numero')
    return render(request, 'mesas/mesas.html', {'mesas': mesas})

def abrir_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if mesa.estado == 'libre':
        pedido = Pedido.objects.create(mesa=mesa)
        mesa.estado = 'ocupada'
        mesa.save()
    else:
        pedido = Pedido.objects.filter(mesa=mesa, cerrado=False).first()
    productos = Producto.objects.all()
    detalles = pedido.detalles.all()
    return render(request, 'mesas/pedido.html', {
        'mesa': mesa,
        'pedido': pedido,
        'productos': productos,
        'detalles': detalles,
    })
def agregar_producto(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))
        producto = get_object_or_404(Producto, id=producto_id)

        if cantidad > producto.stock:
            cantidad = producto.stock

        if cantidad > 0:
            detalle, creado = DetallePedido.objects.get_or_create(
                pedido=pedido,
                producto=producto,
                defaults={'cantidad': cantidad, 'precio_unitario': producto.precio}
            )
            if not creado:
                detalle.cantidad += cantidad
                detalle.save()
            producto.stock -= cantidad
            producto.save()
            total = sum(d.subtotal() for d in pedido.detalles.all())
            pedido.total = total
            pedido.save()
    return redirect('abrir_mesa', mesa_id=pedido.mesa.id)


def cerrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.cerrado = True
    pedido.save()
    pedido.mesa.estado = 'libre'
    pedido.mesa.save()
    from ventas.models import Venta
    Venta.objects.create(pedido=pedido, total=pedido.total)
    return redirect('mesas')

def eliminar_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)
    if mesa.estado == 'libre':
        mesa.delete()
    return redirect('mesas')