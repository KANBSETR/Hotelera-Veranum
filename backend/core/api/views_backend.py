from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.api.serializers import *
from core.models import *

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from rest_framework import generics

#Toda clase con ListCreateAPIView es para listar y crear en json
class RegionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    
class GeneroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class CargoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class PersonaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
class UsuarioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmpleadoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoHabitacionListCreateAPIView(generics.ListCreateAPIView):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

class RegistroServicioAdicionalListCreateAPIView(generics.ListCreateAPIView):
    queryset = RegistroServicioAdicional.objects.all()
    serializer_class = RegistroServicioAdicionalSerializer

class HotelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RegistroHabitacionListCreateAPIView(generics.ListCreateAPIView):
    queryset = RegistroHabitacion.objects.all()
    serializer_class = RegistroHabitacionSerializer


# Toda clase con RetrieveUpdateDestroyAPIView es para ver, actualizar y eliminar en json
class RegionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProvinciaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ComunaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    
    
class GeneroDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class CargoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class PersonaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class UsuarioDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmpleadoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class CategoriaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoHabitacionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

class RegistroServicioAdicionalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistroServicioAdicional.objects.all()
    serializer_class = RegistroServicioAdicionalSerializer

class HotelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RegistroHabitacionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistroHabitacion.objects.all()
    serializer_class = RegistroHabitacionSerializer

class ReservaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer









"""
  def patch(self,request, pk=None):
        try:
            avion = get_object_or_404(Avion, pk=pk) #enMantenimiento=True
            serializer = AvionSerializer(avion, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"message": "La operación viola una restricción de integridad en la base de datos"}, 
                        status=status.HTTP_400_BAD_REQUEST)
"""