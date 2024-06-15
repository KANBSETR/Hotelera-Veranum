from django.forms import ModelForm, UserCreationForm
from core.models import *

class EmpleadoForm(UserCreationForm):
    class Meta:
        model = Empleado
        fields = UserCreationForm.Meta.fields + ['rut', 'roles']

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = UserCreationForm.Meta.fields + ['id_usuario']