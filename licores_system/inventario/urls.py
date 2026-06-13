from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario_lista, name='inventario'),
    path('agregar/', views.agregar_producto, name='agregar_producto_inventario'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]