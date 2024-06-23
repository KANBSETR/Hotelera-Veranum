from django.urls import path
from inventario import views

urlpatterns = [
    path('inventarioListar/', views.inventario, name='inventario')
]