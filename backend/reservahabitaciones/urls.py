from django.urls import path
from reservahabitaciones import views



urlpatterns = [
    path('',views.reservar_habitacion, name='reservar_habitacion'),
    path('listarReservas/',views.listar_reservas, name='listar_reservas'),
        #ACTUALIZAR
    path('actualizarReserva/<int:id_reserva>/',views.reserva_detail, name='reserva_detail'),
    path('registrarReserva/',views.agregarReserva, name='agregarReserva'),
    path('actualizarReserva/<int:id_reserva>/delete',views.reserva_delete, name='reserva_delete'),

]