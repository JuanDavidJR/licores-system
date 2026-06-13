from django.urls import path
from . import views

urlpatterns = [
    path('', views.mesas_lista, name='mesas'),
    path('abrir/<int:mesa_id>/', views.abrir_mesa, name='abrir_mesa'),
    path('agregar_producto/<int:pedido_id>/', views.agregar_producto, name='agregar_producto'),
    path('cerrar/<int:pedido_id>/', views.cerrar_pedido, name='cerrar_pedido'),
    path('eliminar/<int:mesa_id>/', views.eliminar_mesa, name='eliminar_mesa'),
]