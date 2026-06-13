from django.contrib import admin
from .models import Mesa, Pedido, DetallePedido

admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(DetallePedido)