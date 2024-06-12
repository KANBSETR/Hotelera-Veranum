from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario, name='formulario'),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('signup/', views.signup, name='signup')
]