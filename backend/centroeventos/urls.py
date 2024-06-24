from django.urls import path
from centroeventos import views



urlpatterns = [
    path('listarEvento/',views.listar_eventos, name='listar_eventos'),
        #ACTUALIZAR
    path('actualizarEvento/<int:idEvento>/',views.evento_detail, name='evento_detail'),
    path('registrarEvento/',views.agregarEvento, name='agregarEvento'),
    path('actualizarEvento/<int:idEvento>/delete',views.evento_delete, name='evento_delete'),

]