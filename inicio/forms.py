from django import forms

class CrearProducto(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'}))
    precio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Precio...'}))
    stock = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Stock...'}))
    
class BuscarProducto(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'})) 