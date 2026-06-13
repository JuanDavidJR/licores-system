from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mesas/', include('mesas.urls')),
    path('inventario/', include('inventario.urls')),
    path('ventas/', include('ventas.urls')),
    path('', include('mesas.urls')),
]