from django import forms
from .models import Persona, Empleado, Usuario, Comuna, Genero
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re #Para validar el RUT ya que manipula cadenas basandose en patrones espcificos



def validate_not_all_numeric(value):
    if value.isdigit():
        raise ValidationError(
            'La contraseña no puede ser completamente numérica.',
            params={'value': value},
        )
def format_rut(rut):
    rut = rut[::-1]
    rut_formateado = '-'.join([rut[i:i+3][::-1] for i in range(0, len(rut), 3)])[::-1]
    return rut_formateado

class PersonaForm(forms.ModelForm):
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())
    genero = forms.ModelChoiceField(queryset=Genero.objects.all())

    rut = forms.CharField(
        max_length=9,
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El RUT debe tener un máximo de 9 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: 12.345.678-3'})
    )
    nombre = forms.CharField(
        max_length=50,
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El nombre debe tener un máximo de 50 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: Juan'})
    )
    apPaterno = forms.CharField(
        max_length=50,
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El apellido paterno debe tener un máximo de 50 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: Perez'})
    )
    apMaterno = forms.CharField(
        max_length=50,
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El apellido materno debe tener un máximo de 50 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: Garcia'})
    )
    email = forms.EmailField(
        max_length=80,
        label='Correo electrónico',
        validators=[EmailValidator(message="Debe ser una dirección de correo electrónico válida.")],
        widget=forms.EmailInput(attrs={'placeholder': 'ej: correo@gmail.com'})
    )    
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())
    genero = forms.ModelChoiceField(queryset=Genero.objects.all())
    telefono = forms.CharField(
        max_length=12,
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El teléfono debe tener un máximo de 12 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: +56912345678'})
    )
    
    # Se define o se especifica el formulario el modelo de datos que se utilizara y los campos, formulario django
    class Meta:
        model = Persona
        fields = ['rut', 'nombre', 'apPaterno', 'apMaterno', 'email','comuna','genero','telefono']

    
    #def clean_dv(self):
    #    dv = self.cleaned_data['dv']
    #    if not dv:
    #        raise forms.ValidationError("Debe ingresar un Digito Verificador")
    #    return dv
    
    
    # Este método se ejecuta cuando se crea una instancia del formulario
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['telefono'].label = "Número de celular"
        self.fields['telefono'].widget.attrs.update({'placeholder': 'ej: +56912345678'})
 
    #Valida campo rut


    
    #def clean_rut(self):
    #    rut = self.cleaned_data.get('rut')
    #    pattern = r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$'        
    #    if not re.match(pattern, rut):
    #        raise ValidationError("El RUT debe estar en el formato correcto (XX.XXX.XXX-X).")
    #    if Persona.objects.filter(rut=rut).exists():
    #        raise ValidationError("Este RUT ya está en uso.")
    #    return rut
    
    #Validar campo first_name
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Transforma la primera letra de cada palabra a mayúscula
        nombre = ' '.join(word.capitalize() for word in nombre.split())
        return nombre

    #Lo mismo
    def clean_ap_paterno(self):
        apPaterno = self.cleaned_data.get('apPaterno')
        # Transforma la primera letra de cada palabra a mayúscula
        apPaterno = ' '.join(word.capitalize() for word in apPaterno.split())
        return apPaterno
    
    def clean_ap_materno(self):
        apMaterno = self.cleaned_data.get('apMaterno')
        # Transforma la primera letra de cada palabra a mayúscula
        apMaterno = ' '.join(word.capitalize() for word in apMaterno.split())
        return apMaterno
    
    #email = forms.EmailField()
    #Lo mismin
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Persona.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        return email
        
    
    
    
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'rut', 'usuario','clave','codCargo','sueldo','clave']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'rut','usuario','clave']