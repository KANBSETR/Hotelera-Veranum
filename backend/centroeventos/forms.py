from django import forms
from core.models import Eventos

class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['nombre', 'fechaInicio', 'fechaTermino', 'descripcion', 'precio', 'estado', 'idHotel', 'idFormaPago', 'idEmpleado', 'idUsuario']