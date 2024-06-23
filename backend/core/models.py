from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import  Group, Permission
from django.utils.crypto import get_random_string
import uuid
from django.utils import timezone
from datetime import date



class Region (models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Provincia (models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.nombre + ', Region' + self.id_region.nombre

class Comuna (models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nombre + ', Provincia' + self.id_provincia.nombre

class Genero(models.Model):
    idGenero  = models.AutoField( primary_key=True,db_column='id_genero')
    nombre     = models.CharField(max_length=20, blank=False, null=False,db_column='genero')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)

    # def __init__(self,id,codigo=None,genero=None):
    #     self.idGenero=id
    #     self.codigo=codigo
    #     self.genero=genero

    def __str__(self):
        return self.nombre
    
 
"""
 USER_TYPE_CHOICES = (
      (1, 'Usuario'),
      (2, 'Empleado'),
      (3, 'Admin')
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)    
"""
class Persona(models.Model):
    rut    = models.IntegerField(primary_key=True)
    dv    = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apPaterno = models.CharField(max_length=30, blank=True, null=True)
    apMaterno = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=False)
    fechaNacimiento = models.DateField(auto_now_add=True, blank=True, null=True,db_column='fecha_nacimiento')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    genero        = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero')
    telefono = models.CharField(max_length=15)
    

    
    def __str__(self):
        return f'{self.nombre} {self.apPaterno} {self.apMaterno}'


class Cargo(models.Model): #steve
    idCargo = models.AutoField(null=False, primary_key=True, db_column='codCargo')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    OPCIONES_CARGO = [
        ('Usuario', 'Usuario normal'),
        ('EncargadoHabitacion', 'Encargado de Habitaciones'),
        ('EncargadoInventario', 'Encargado de Inventario'),
        ('EncargadoServAdicional', 'Encargado de Servicios Adicionales'),
        ('EncargadoReserva', 'Encargado de Reservas'),
        ('EncargadoMantencion', 'Encargado de Mantención'),
        ('EncargadoFinanzas', 'Encargado de Finanzas'),
        ('EncargadoCliente', 'Encargado de Clientes'),
        ('EncargadoRestaurante', 'Encargado de Restaurante'),
        ('EncargadoBar', 'Encargado de Bar'),
        ('EncargadoSpa', 'Encargado de Spa'),
        ('EncargadoPiscina', 'Encargado de Piscina'),
        ('EncargadoGimnasio', 'Encargado de Gimnasio'),
        ('EncargadoSalonEventos', 'Encargado de Salón de Eventos'),
        ('EncargadoTienda', 'Encargado de Tienda'),
        ('EncargadoCocina', 'Encargado de Cocina'),
        ('EncargadoLavanderia', 'Encargado de Lavandería'),
        ('EncargadoRecepcion', 'Encargado de Recepción'),
        ('EncargadoSeguridad', 'Encargado de Seguridad'),
        ('EncargadoMascotas', 'Encargado de Mascotas'),
        ('EncargadoJardineria', 'Encargado de Jardinería'),
        ('EncargadoAseo', 'Encargado de Aseo'),
        ('EncargadoMensajeria', 'Encargado de Mensajería'),
        ('EncargadoEstacionamiento', 'Encargado de Estacionamiento'),
        ('EncargadoMantVehiculos', 'Encargado de Mantención de Vehículos'),
        ('EncargadoMantMaquinaria', 'Encargado de Mantención de Maquinaria'),
        ('EncargadoMantEquipos', 'Encargado de Mantención de Equipos'),
        ('EncargadoMantInfraestructura', 'Encargado de Mantención de Infraestructura'),
        ('EncargadoMantTecnologia', 'Encargado de Mantención de Tecnología'),
        ('EncargadoMantRedes', 'Encargado de Mantención de Redes'),
        ('EncargadoMantSistemas', 'Encargado de Mantención de')
    ]
    nombreCargo = models.CharField(max_length=100)

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)  
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    usuario = models.CharField(max_length=20, null=False)
    clave = models.CharField(max_length=10, null=False)
    codCargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    sueldo = models.IntegerField(null=False)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return f'Empleado: {self.rut.nombre} {self.rut.apPaterno}'    

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    usuario=models.CharField(unique=True,max_length=20, null=False)
    clave=models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.usuario
    
#Ej: vip, nose ,normal ,etc
class Categoria (models.Model):
        id_categoria = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        
        OPCIONES_CATEGORIA = [
            ('Vip', 'Vip'),
            ('Normal', 'Normal'),
            ('Economico', 'Economico'),
            ('Familiar', 'Familiar'),
            ('Suite', 'Suite'),
            ('Presidencial', 'Presidencial')
        ]
        
        categorias = models.CharField(max_length=50, choices=OPCIONES_CATEGORIA, default='Normal')
        
        def __str__(self):
            return self.nombre
        
#Ej: habitacion simple, doble, triple, etc
class TipoHabitacion (models.Model):
        id_tipo_habitacion = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        
        OPCIONES_TIPO_HABITACION = [
            ('Simple', 'Simple'),
            ('Doble', 'Doble'),
            ('Triple', 'Triple'),
            ('Matrimonial', 'Matrimonial'),
        ]
        
        tipos_habitaciones = models.CharField(max_length=50, choices=OPCIONES_TIPO_HABITACION, default='Simple')
        
        def __str__(self):
            return self.nombre

#Ej: wifi, tv, etc
class RegistroServicioAdicional (models.Model):
        id_servicio = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=50)
        precio = models.IntegerField()
        
        
        def __str__(self):
            return self.nombre
        
class Hotel (models.Model):
        id_hotel = models.AutoField(primary_key=True)
        patente_hotel = models.CharField(max_length=50)
        nombre = models.CharField(max_length=50)
        telefono = models.CharField(max_length=50)
        correo = models.EmailField()
        direccion = models.CharField(max_length=50)
        total_habitaciones_hotel = models.IntegerField()
        estado_habitacion = models.BooleanField()        
        id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.nombre

class RegistroHabitacion (models.Model):
        id_habitacion = models.AutoField(primary_key=True)
        numero_habitacion = models.IntegerField()
        cant_dormitorios = models.IntegerField()
        cant_banos = models.IntegerField()
        cant_camas = models.IntegerField()
        tamano_camas = models.CharField(max_length=50)
        cant_personas_disp = models.IntegerField()
        descripcion = models.CharField(max_length=50)
        precio = models.IntegerField()
        estado_habitacion = models.BooleanField()
        id_servicio = models.ForeignKey(RegistroServicioAdicional, on_delete=models.CASCADE)
        id_tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
        id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
        id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
       
        def __str__(self):
            return self.descripcion
        
#Requerimiento 13 al 17 - Inventario
class HotelDetalle (models.Model):
        id_hotel_detalle = models.AutoField(primary_key=True)
        descripcion = models.CharField(max_length=350)
        id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
        id_tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
        id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        id_registro_servicio_adicional = models.ForeignKey(RegistroServicioAdicional, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.nombre
        
        
class FormaPago(models.Model): 
    idFPago = models.AutoField(null=False, primary_key=True,db_column='codFormaPago')
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200, null=False,db_column='descripcion')
    
    def __str__(self):
        return self.nombre

class Eventos(models.Model):
    idEvento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField()
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    estado = models.BooleanField()
    idHotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='idHotel')
    idFormaPago = models.ForeignKey(FormaPago, models.DO_NOTHING, db_column='idFormaPago')
    idEmpleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idEmpleado')
    idUsuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='idUsuario')
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    fModificacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fechaInicio = models.DateTimeField()
    fechaTermino = models.DateTimeField()
    estado = models.BooleanField()
    idHabitacion = models.ForeignKey(RegistroHabitacion, on_delete=models.CASCADE)
    idHotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.idReserva







# Codigo en caso de:
"""
#Registro de usuarios que utilizaran la pagina
class RegistroCuentaUsuario (models.Model):
    #Campos de texto
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=50)
    #Campos de fecha
    fecha_nacimiento = models.DateField() # Poner que de la edad solo
    fecha_creacion = models.DateTimeField(auto_now_add=True) #Fecha de creacion de la cuenta
    ultimo_acceso = models.DateTimeField(auto_now=True) # Ultimo acceso a la acuenta registrado
    #Foraneas
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.nombre_usuario = self.correo.split('@')[0]  # Extrae la parte antes del '@' en el correo
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre



#Solo el admin puede manejar estos registros
class RegistroCuentaEmpleados(models.Model):
    # Campos de texto
    rut = models.CharField(max_length=10, unique=True, primary_key=True, help_text="Ingrese el RUT sin puntos ni guión")    
    nombre_usuario = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    correo_alternativo = models.EmailField(null=True, blank=True)
    contrasena = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    # Campos de fecha
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(auto_now=True)
    # Foraneas
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    OPCIONES_ROL = [
        ('Usuario', 'Usuario normal'),
        ('EncargadoHabitacion', 'Encargado de Habitaciones'),
        ('EncargadoInventario', 'Encargado de Inventario'),
        ('EncargadoServAdicional', 'Encargado de Servicios Adicionales'),
        ('EncargadoReserva', 'Encargado de Reservas'),
        ('EncargadoMantencion', 'Encargado de Mantención'),
        ('EncargadoFinanzas', 'Encargado de Finanzas'),
        ('EncargadoCliente', 'Encargado de Clientes'),
        ('EncargadoRestaurante', 'Encargado de Restaurante'),
        ('EncargadoBar', 'Encargado de Bar'),
        ('EncargadoSpa', 'Encargado de Spa'),
        ('EncargadoPiscina', 'Encargado de Piscina'),
        ('EncargadoGimnasio', 'Encargado de Gimnasio'),
        ('EncargadoSalonEventos', 'Encargado de Salón de Eventos'),
        ('EncargadoTienda', 'Encargado de Tienda'),
        ('EncargadoCocina', 'Encargado de Cocina'),
        ('EncargadoLavanderia', 'Encargado de Lavandería'),
        ('EncargadoRecepcion', 'Encargado de Recepción'),
        ('EncargadoSeguridad', 'Encargado de Seguridad'),
        ('EncargadoMascotas', 'Encargado de Mascotas'),
        ('EncargadoJardineria', 'Encargado de Jardinería'),
        ('EncargadoAseo', 'Encargado de Aseo'),
        ('EncargadoMensajeria', 'Encargado de Mensajería'),
        ('EncargadoEstacionamiento', 'Encargado de Estacionamiento'),
        ('EncargadoMantVehiculos', 'Encargado de Mantención de Vehículos'),
        ('EncargadoMantMaquinaria', 'Encargado de Mantención de Maquinaria'),
        ('EncargadoMantEquipos', 'Encargado de Mantención de Equipos'),
        ('EncargadoMantInfraestructura', 'Encargado de Mantención de Infraestructura'),
        ('EncargadoMantTecnologia', 'Encargado de Mantención de Tecnología'),
        ('EncargadoMantRedes', 'Encargado de Mantención de Redes'),
        ('EncargadoMantSistemas', 'Encargado de Mantención de')
    ]
    
    roles = models.CharField(max_length=50, choices=OPCIONES_ROL, default='Usuario')
    
    def validate_unique(self, exclude=None):
        exclude = ('rut',) if exclude is None else tuple(exclude) + ('rut',)
        super().validate_unique(exclude=exclude)
        
    def __str__(self):
        if self.nombre_usuario == 'admin':
            return 'Usuario admin'
        return f'Usuario: {self.nombre_usuario} - Rut: {str(self.rut)}'
    
    def __str__(self):
        if self.nombre_usuario == 'empleado':
            return 'Usuario empleado'
        return f'Usuario: {self.nombre_usuario} - Rut: {str(self.rut)}'
    
    
"""
    


"""
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('fecha_nacimiento', date.today())  # Valor por defecto para fecha_nacimiento
        extra_fields.setdefault('id_comuna', 1)  
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 3)  # 3 es para 'Admin'
        return self.create_user(username, email, password, **extra_fields)
"""    