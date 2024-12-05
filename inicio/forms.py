from django import forms

class CrearProducto(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.CharField()
    stock = forms.IntegerField()
    
class BuscarProducto(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre...'})) 