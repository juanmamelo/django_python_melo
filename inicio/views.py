from django.shortcuts import render
from inicio.models import Producto
from inicio.forms import CrearProducto, BuscarProducto

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_producto(request):
    formulario = CrearProducto()
    if request.method == 'POST':
        formulario = CrearProducto(request.POST)
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            producto = Producto(nombre=data.get("nombre"), precio=data.get("precio"), stock=data.get("stock"))
            producto.save()
            return render(request, 'inicio/producto_creacion_correcta.html')
        
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