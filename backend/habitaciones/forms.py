from django.forms import ModelForm
from core.models import RegistroHabitacion

class HabitacionForm(ModelForm):
    class Meta:
        model = RegistroHabitacion
        fields = ['numero_habitacion', 'cant_dormitorios', 'cant_banos','cant_camas','tamano_camas',
                  'cant_personas_disp','descripcion','precio','estado_habitacion','id_servicio',
                  'id_tipo_habitacion','id_empleado','id_hotel']


