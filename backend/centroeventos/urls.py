from django.urls import path
from centroeventos import views



urlpatterns = [
    path('listarEventos/', views.eventos, name='eventos')

]