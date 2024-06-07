from django.urls import path
from habitaciones import views



urlpatterns = [
    path('listarHabitacion/',views.listar_habitaciones, name='listar_habitaciones'),
        #ACTUALIZAR
    path('actualizarHabitacion/<int:id_habitacion>/',views.habitacion_detail, name='habitacion_detail'),
    path('registrarHabitacion/',views.agregarHabitacion, name='agregarHabitacion'),
    path('actualizarHabitacion/<int:id_habitacion>/delete',views.habitacion_delete, name='habitacion_delete'),

]