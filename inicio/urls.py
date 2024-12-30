from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about_me, name='about_me'),
    path('productos/ ', views.listado_productos, name='listado_productos'),
    path('productos/crear/ ', views.crear_producto, name='crear_producto'),
    path('producto_creacion_correcta/', views.producto_creacion_correcta, name='producto_creacion_correcta'),
    path('productos/<int:id_producto>/ ', views.ver_producto, name='ver_producto'),
    path('productos/<int:id_producto>/editar/ ', views.editar_producto, name='editar_producto'),
    path('productos/<int:id_producto>/eliminar/ ', views.eliminar_producto, name='eliminar_producto'),
]