from django import forms
from core.models import Eventos

class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['nombre', 'fechaInicio', 'fechaTermino', 'descripcion', 'precio', 'estado', 'idHotel', 'idFormaPago', 'idEmpleado', 'idUsuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInicio': forms.DateTimeInput(attrs={'class': 'form-control',  'type': 'datetime-local'}),
            'fechaTermino': forms.DateTimeInput(attrs={'class': 'form-control',  'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'idHotel': forms.Select(attrs={'class': 'form-control'}),
            'idFormaPago': forms.Select(attrs={'class': 'form-control'}),
            'idEmpleado': forms.Select(attrs={'class': 'form-control'}),
            'idUsuario': forms.Select(attrs={'class': 'form-control'}),
        }