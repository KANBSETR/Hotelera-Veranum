from django.forms import ModelForm
from core.models import HotelDetalle
from django import forms

class InventarioForm(ModelForm):
    class Meta:
        model = HotelDetalle
        fields = ['id_hotel', 'descripcion', 'id_tipo_habitacion', 'id_categoria', 'id_registro_servicio_adicional']
        labels = {
            'id_hotel': 'Hotel',
            'descripcion': 'Descripción',
            'id_tipo_habitacion': 'Tipo de Habitación',
            'id_categoria': 'Categoría',
            'id_registro_servicio_adicional': 'Servicio Adicional'
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }
        