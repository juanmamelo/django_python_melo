from django.urls import path
from inicio.views import crear_producto, producto_creacion_correcta, listado_productos, inicio

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/ ', listado_productos, name='listado_productos'),
    path('productos/crear/ ', crear_producto, name='crear_producto'),
    path('producto_creacion_correcta/', producto_creacion_correcta, name='producto_creacion_correcta')
]