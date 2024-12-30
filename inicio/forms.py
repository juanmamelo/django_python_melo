from django import forms

class CrearProducto(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput())
    precio = forms.CharField(widget=forms.TextInput())
    stock = forms.IntegerField(widget=forms.TextInput())
    fecha_agregado = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    imagen = forms. ImageField(required=False)
    
class BuscarProducto(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'})) 
    
class EditarProducto(CrearProducto):
    ...