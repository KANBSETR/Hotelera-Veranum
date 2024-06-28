from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.register, name='register'),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'),
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('usuarios/', views.usuario, name='usuario'),
]