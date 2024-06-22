from django.forms import ModelForm
from core.models import RegistroServicioAdicional

class ServicioAdForm(ModelForm):
    class Meta:
        model = RegistroServicioAdicional
        fields = ['nombre', 'descripcion','precio']


