from django.contrib import admin
from .models import *

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria','nombre','descripcion','categorias']

@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ['id_tipo_habitacion','nombre','descripcion','id_categoria','tipos_habitaciones']

@admin.register(RegistroServicioAdicional)
class RegistroServicioAdicionalAdmin(admin.ModelAdmin):
    list = ['id_servicio','nombre','descripcion','servicios_ad']
    
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id_region','nombre']

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ['id_provincia','nombre','id_region']

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ['id_comuna','nombre','id_provincia']
    
@admin.register(RegistroCuentaEmpleados)
class RegistroCuentaEmpleadosAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre_usuario','nombre','ap_paterno','ap_materno',
                    'correo_alternativo','contrasena','telefono','direccion','fecha_nacimiento',
                    'fecha_creacion','ultimo_acceso','id_comuna','roles']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id_hotel','patente_hotel','nombre','telefono','correo','direccion',
                    'total_habitaciones_hotel','estado_habitacion','id_comuna']

@admin.register(RegistroHabitacion)
class RegistroHabitacionAdmin(admin.ModelAdmin):
    list_display = ['id_habitacion','numero_habitacion','cant_dormitorios','cant_banos',
                    'cant_camas','tamano_camas','cant_personas_disp','descripcion','precio',
                    'estado_habitacion','id_servicio','id_tipo_habitacion','id_empleado','id_hotel']
    
    