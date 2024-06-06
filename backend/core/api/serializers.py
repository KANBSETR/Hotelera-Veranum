from rest_framework import serializers
from ..models import *

class RegionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ProvinciaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class ComunaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'
        
class RegistroCuentaUsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = RegistroCuentaUsuario
        fields = '__all__'

class RegistroCuentaEmpleadosSerializer (serializers.ModelSerializer):
    class Meta:
        model = RegistroCuentaEmpleados
        fields = '__all__'

class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TipoHabitacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'

class RegistroServicioAdicionalSerializer (serializers.ModelSerializer):
    class Meta:
        model = RegistroServicioAdicional
        fields = '__all__'

class HotelSerializer (serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RegistroHabitacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = RegistroHabitacion
        fields = '__all__'

        