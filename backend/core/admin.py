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

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['idGenero','nombre']


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['idCargo','nombreCargo']

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'comuna']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['rut', 'idUsuario', 'usuario']
    
    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'idEmpleado', 'codCargo']
    
    
    
    
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id_hotel','patente_hotel','nombre','telefono','correo','direccion',
                    'total_habitaciones_hotel','estado_habitacion','id_comuna']

@admin.register(RegistroHabitacion)
class RegistroHabitacionAdmin(admin.ModelAdmin):
    list_display = ['id_habitacion','numero_habitacion','cant_dormitorios','cant_banos',
                    'cant_camas','tamano_camas','cant_personas_disp','descripcion','precio',
                    'estado_habitacion','id_servicio','id_tipo_habitacion','id_empleado','id_hotel']
    

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ['nombre','fechaInicio','fechaTermino','descripcion','precio','estado','idHotel','idFormaPago','idEmpleado','idUsuario']
    
@admin.register(FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre']