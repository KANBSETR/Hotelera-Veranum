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

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'id_comuna']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'get_email', 'get_ap_paterno', 'get_ap_materno', 'get_nombre', 'get_fecha_nacimiento', 'get_fecha_creacion', 'get_ultimo_acceso']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'  

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    
    def get_ap_paterno(self, obj):
        return obj.ap_paterno
    get_ap_paterno.short_description = 'ap_paterno'
    
    def get_ap_materno(self, obj):
        return obj.ap_materno
    get_ap_materno.short_description = 'ap_materno'
    
    def get_nombre(self, obj):
        return obj.nombre
    get_nombre.short_description = 'Nombre'
    
    def get_fecha_nacimiento(self, obj):
        return obj.fecha_nacimiento
    get_fecha_nacimiento.short_description = 'Fecha Nacimiento'
    
    def get_fecha_creacion(self, obj):
        return obj.fecha_creacion
    get_fecha_creacion.short_description = 'Fecha Creacion'
    
    def get_ultimo_acceso(self, obj):
        return obj.ultimo_acceso
    get_ultimo_acceso.short_description = 'Ultimo Acceso'
    
    
    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'rut', 'get_email', 'get_ap_paterno', 'get_ap_materno', 'get_nombre', 'get_fecha_nacimiento', 'get_fecha_creacion', 'get_ultimo_acceso', 'roles']
    
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'  

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    
    def get_ap_paterno(self, obj):
        return obj.user.ap_paterno
    get_ap_paterno.short_description = 'ap_paterno'
    
    def get_ap_materno(self, obj):
        return obj.user.ap_materno
    get_ap_materno.short_description = 'ap_materno'
    
    def get_nombre(self, obj):
        return obj.user.nombre
    get_nombre.short_description = 'Nombre'
    
    def get_fecha_nacimiento(self, obj):
        return obj.user.fecha_nacimiento
    get_fecha_nacimiento.short_description = 'Fecha Nacimiento'
    
    def get_fecha_creacion(self, obj):
        return obj.user.fecha_creacion
    get_fecha_creacion.short_description = 'Fecha Creacion'
    
    def get_ultimo_acceso(self, obj):
        return obj.user.ultimo_acceso
    get_ultimo_acceso.short_description = 'Ultimo Acceso'
    

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id_hotel','patente_hotel','nombre','telefono','correo','direccion',
                    'total_habitaciones_hotel','estado_habitacion','id_comuna']

@admin.register(RegistroHabitacion)
class RegistroHabitacionAdmin(admin.ModelAdmin):
    list_display = ['id_habitacion','numero_habitacion','cant_dormitorios','cant_banos',
                    'cant_camas','tamano_camas','cant_personas_disp','descripcion','precio',
                    'estado_habitacion','id_servicio','id_tipo_habitacion','id_empleado','id_hotel']
    
    