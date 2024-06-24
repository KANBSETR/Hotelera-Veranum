from django.forms import ModelForm
from core.models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['fechaInicio', 'fechaTermino','estado','idHabitacion','idHotel','idUsuario']

