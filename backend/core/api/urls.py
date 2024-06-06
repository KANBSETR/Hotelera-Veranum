from django.urls import path, include
from core.api.views_backend import *


urlpatterns = [
    # Toda clase con ListCreateAPIView es para listar y crear en json
    path('api/regiones/', RegionListCreateAPIView.as_view(), name='region-list'),
    path('api/provincias/', ProvinciaListCreateAPIView.as_view(), name='provincia-list'),
    path('api/comunas/', ComunaListCreateAPIView.as_view(), name='comuna-list'),
    path('api/registro-cuenta-usuario/', RegistroCuentaUsuarioListCreateAPIView.as_view(), name='registro-cuenta-usuario-list'),
    path('api/registro-cuenta-empleados/', RegistroCuentaEmpleadosListCreateAPIView.as_view(), name='registro-cuenta-empleados-list'),
    path('api/categorias/', CategoriaListCreateAPIView.as_view(), name='categoria-list'),
    path('api/tipo-habitacion/', TipoHabitacionListCreateAPIView.as_view(), name='tipo-habitacion-list'),
    path('api/registro-servicio-adicional/', RegistroServicioAdicionalListCreateAPIView.as_view(), name='registro-servicio-adicional-list'),
    path('api/hoteles/', HotelListCreateAPIView.as_view(), name='hotel-list'),
    path('api/registro-habitacion/', RegistroHabitacionListCreateAPIView.as_view(), name='registro-habitacion-list'),
    # Toda clase con RetrieveUpdateDestroyAPIView es para ver, actualizar y eliminar en json
    path('api/regiones/<int:pk>/', RegionDetailAPIView.as_view(), name='region-detail'),
    path('api/provincias/<int:pk>/', ProvinciaDetailAPIView.as_view(), name='provincia-detail'),
    path('api/comunas/<int:pk>/', ComunaDetailAPIView.as_view(), name='comuna-detail'),
    path('api/registro-cuenta-usuario/<int:pk>/', RegistroCuentaUsuarioDetailAPIView.as_view(), name='registro-cuenta-usuario-detail'),
    path('api/registro-cuenta-empleados/<int:pk>/', RegistroCuentaEmpleadosDetailAPIView.as_view(), name='registro-cuenta-empleados-detail'),
    path('api/categorias/<int:pk>/', CategoriaDetailAPIView.as_view(), name='categoria-detail'),
    path('api/tipo-habitacion/<int:pk>/', TipoHabitacionDetailAPIView.as_view(), name='tipo-habitacion-detail'),
    path('api/registro-servicio-adicional/<int:pk>/', RegistroServicioAdicionalDetailAPIView.as_view(), name='registro-servicio-adicional-detail'),
    path('api/hoteles/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel-detail'),
    path('api/registro-habitacion/<int:pk>/', RegistroHabitacionDetailAPIView.as_view(), name='registro-habitacion-detail'),
]