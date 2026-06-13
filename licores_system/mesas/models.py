
# Create your models here.
from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    estado = models.CharField(max_length=20, choices=[
        ('libre', 'Libre'),
        ('ocupada', 'Ocupada'),
    ], default='libre')

    def __str__(self):
        return f'Mesa {self.numero}'


class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='pedidos')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cerrado = models.BooleanField(default=False)

    def __str__(self):
        return f'Pedido #{self.id} - Mesa {self.mesa.numero}'


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario