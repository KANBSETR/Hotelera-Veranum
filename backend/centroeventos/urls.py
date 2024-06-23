from django.urls import path
from centroeventos import views



urlpatterns = [
<<<<<<< HEAD
    path('listarEventos/', views.eventos, name='eventos')
=======
    path('listarEvento/',views.listar_eventos, name='listar_eventos'),
        #ACTUALIZAR
    path('actualizarEvento/<int:idEvento>/',views.evento_detail, name='evento_detail'),
    path('registrarEvento/',views.agregarEvento, name='agregarEvento'),
    path('actualizarEvento/<int:idEvento>/delete',views.evento_delete, name='evento_delete'),
>>>>>>> 8b440665b871ba0a90c3da1b0d3f4c9c53eb5339

]