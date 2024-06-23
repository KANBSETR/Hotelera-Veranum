from django.urls import path
from . import views


urlpatterns = [
    path('formulario/', views.register, name='register'),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'),
    path('inicio/', views.inicio, name='inicio'),
]