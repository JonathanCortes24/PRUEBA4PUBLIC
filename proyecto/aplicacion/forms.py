from django import forms
from django.forms import fields
from .models import Vehiculos

class VehiculoFormulario(forms.ModelForm):
    class Meta: 
        model = Vehiculos
        fields = ('marca', 'modelo', 'vin', 'patente', 'año_de_fabricacion', 'fecha_de_recepcion')