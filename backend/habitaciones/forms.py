from django.forms import ModelForm
from core.models import RegistroHabitacion

class HabitacionForm(ModelForm):
    class Meta:
        model = RegistroHabitacion
        fields = ['numero_habitacion', 'cant_dormitorios', 'cant_banos','cant_camas','tamano_camas',
                  'cant_personas_disp','descripcion','precio','estado_habitacion','id_servicio',
                  'id_tipo_habitacion','id_empleado','id_hotel']
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


