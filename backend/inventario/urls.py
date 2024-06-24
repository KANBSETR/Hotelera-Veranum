from django.urls import path
from inventario import views

urlpatterns = [
    path('listarInventario/',views.listar_inventario, name='listar_inventario'),
        #ACTUALIZAR
    path('actualizarInventario/<int:id_inventario>/',views.inventario_detail, name='inventario_detail'),
    path('registrarInventario/',views.agregarInventario, name='agregarInventario'),
    path('actualizarInventario/<int:id_inventario>/delete',views.inventario_delete, name='inventario_delete'),
]