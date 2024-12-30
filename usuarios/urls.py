from django.urls import path
from usuarios import views


app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', views.login, name='iniciar_sesion'),
    path('cerrar-sesion/', views.CerrarSesion.as_view(), name='cerrar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-contraseña/', views.CambiarContraseña.as_view(), name='cambiar_contraseña'),
]
