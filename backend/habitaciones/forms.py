from django.forms import ModelForm
from core.models import RegistroHabitacion
from django import forms

class HabitacionForm(ModelForm):
    class Meta:
        model = RegistroHabitacion
        fields = ['numero_habitacion', 'cant_dormitorios', 'cant_banos','cant_camas','tamano_camas',
                  'cant_personas_disp','descripcion','precio','estado_habitacion','id_servicio',
                  'id_tipo_habitacion','id_empleado','id_hotel']
        widgets = {
            'numero_habitacion': forms.TextInput(attrs={'class': 'form-control'}),
            'cant_dormitorios': forms.NumberInput(attrs={'class': 'form-control'}),
            'cant_banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'cant_camas': forms.NumberInput(attrs={'class': 'form-control'}),
            'tamano_camas': forms.TextInput(attrs={'class': 'form-control'}),
            'cant_personas_disp': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_habitacion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_servicio': forms.Select(attrs={'class': 'form-control'}),
            'id_tipo_habitacion': forms.Select(attrs={'class': 'form-control'}),
            'id_empleado': forms.Select(attrs={'class': 'form-control'}),
            'id_hotel': forms.Select(attrs={'class': 'form-control'}),
            
            
        }
        labels = {
            'numero_habitacion': 'Número de Habitación',
            'cant_dormitorios': 'Cantidad de Dormitorios',
            'cant_banos': 'Cantidad de Baños',
            'cant_camas': 'Cantidad de Camas',
            'tamano_camas': 'Tamaño de las Camas',
            'cant_personas_disp': 'Capacidad',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'estado_habitacion': 'Estado de la Habitación',
            'id_servicio': 'Servicio',
            'id_tipo_habitacion': 'Tipo de Habitación',
            'id_empleado': 'Empleado',
            'id_hotel': 'Hotel',
        }


