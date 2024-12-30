from django.shortcuts import render, redirect, get_object_or_404
from inicio.models import Producto
from inicio.forms import CrearProducto, BuscarProducto, EditarProducto
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
def crear_producto(request):
    formulario = CrearProducto()
    if request.method == 'POST':
        formulario = CrearProducto(request.POST, request.FILES)
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            fecha_agregada = data.get("fecha_agregado")
            if not fecha_agregada:
                fecha_agregada = timezone.now().date()
            
            producto = Producto(nombre=data.get("nombre"), precio=data.get("precio"), stock=data.get("stock"), fecha_agregado=fecha_agregada, imagen=data.get("imagen"))
            producto.save()
            return redirect ('inicio:producto_creacion_correcta')
        
    return render(request, 'inicio/crear_producto.html', {"formulario": formulario})

def producto_creacion_correcta(request):
    return render(request, 'inicio/producto_creacion_correcta.html')

def listado_productos(request):
    
    formulario_busqueda = BuscarProducto(request.GET)
    
    if formulario_busqueda.is_valid():
        nombre_a_buscar = formulario_busqueda.cleaned_data.get('nombre')
        resultado_productos = Producto.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        resultado_productos = []
        
    formulario_busqueda = BuscarProducto()    
    
    return render(request, 'inicio/listado_productos.html', {'listado_productos': resultado_productos, 'formulario': formulario_busqueda})

def ver_producto(request, id_producto):
    
    producto = Producto.objects.get(id=id_producto)
    
    return render(request, 'inicio/ver_producto.html', {'producto': producto})

@login_required
def eliminar_producto(request, id_producto):
    
    producto = Producto.objects.get(id=id_producto)
    
    producto.delete()
    
    return render(request, 'inicio/eliminar_producto.html', {'producto': producto})

@login_required
def editar_producto(request, id_producto):
    
    producto = Producto.objects.get(id=id_producto)
    
    formulario = EditarProducto(initial={"nombre": producto.nombre, "precio": producto.precio, "stock": producto.stock, "fecha_agregado": producto.fecha_agregado, "imagen": producto.imagen})
    
    if request.method == 'POST':
        formulario = EditarProducto(request.POST, request.FILES)
        if formulario.is_valid():
             producto.nombre = formulario.cleaned_data.get('nombre')
             producto.precio = formulario.cleaned_data.get('precio')
             producto.stock = formulario.cleaned_data.get('stock')
             producto.fecha_agregado = formulario.cleaned_data.get('fecha_agregado')
             if formulario.cleaned_data.get('imagen'):
                producto.imagen = formulario.cleaned_data.get('imagen')
             producto.save()
             return redirect ('inicio:listado_productos')
    return render(request, 'inicio/editar_producto.html', {'formulario': formulario, 'producto': producto})

def about_me(request):
    return render(request, 'inicio/about_me.html')