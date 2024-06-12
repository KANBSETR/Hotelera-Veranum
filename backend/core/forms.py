from django.forms import ModelForm, UserCreationForm
from core.models import *

class EmpleadoForm(UserCreationForm):
    class Meta:
        model = RegistroCuentaEmpleados
        fields = ['rut', 'nombre_usuario', 'nombre', 'ap_paterno', 'ap_materno',
                  'correo_alternativo', 'contrasena', 'telefono','direccion',
                  'fecha_nacimiento','fecha_creacion','ultimo_acceso','id_comuna','roles']
        