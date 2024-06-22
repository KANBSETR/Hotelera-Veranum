from django.urls import path
from serviciosadicionales import views



urlpatterns = [
    path('listarServicioAd/',views.listar_servicios, name='listar_servicios'),
        #ACTUALIZAR
    path('actualizarServicioAd/<int:id_servicio>/',views.servicio_detail, name='servicio_detail'),
    path('registrarServicioAd/',views.agregarServicio, name='agregarServicio'),
    path('actualizarServicioAd/<int:id_servicio>/delete',views.servicio_delete, name='servicio_delete'),

]