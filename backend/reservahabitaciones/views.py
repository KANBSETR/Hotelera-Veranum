from django.shortcuts import render, redirect, get_object_or_404
from core.models import *
from django.http import JsonResponse, HttpResponseNotAllowed
import json

from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservaForm
from core.models import Reserva



def listar_reservas(request):
    reserva_habitacion = Reserva.objects.all()
    return render(request, 'reservaHabitaciones.html', {'reservasHabitacion': reserva_habitacion})




def reserva_detail(request, id_reserva):
    if request.method == 'GET':
        reserva_habitacion = get_object_or_404(Reserva, pk=id_reserva)
        form = ReservaForm(instance=reserva_habitacion)
        return render(request, 'modificarReserva.html', {'reserva_habitacion': reserva_habitacion, 'form': form})
    else:
        try:
            reserva_habitacion = get_object_or_404(Reserva, pk=id_reserva)
            form = ReservaForm(request.POST, instance=reserva_habitacion)
            form.save()
            return redirect('listar_reservas')
        except ValueError:
            return render(request, 'modificarReserva.html', {
                'reserva': reserva_habitacion,
                'form': form,
                'error': 'Error al guardar la reserva'
            })
            
            
            
def agregarReserva(request):
    if request.method == 'GET':
        return render(request, 'agregarReserva.html', {
            'form': ReservaForm})
    else:
        try:
            form = ReservaForm(request.POST)
            newReserva_habitacion = form.save(commit=False)
            newReserva_habitacion.user = request.user
            newReserva_habitacion.save()
            return redirect('listar_reservas')
        except ValueError:
            return render(request, 'agregarReserva.html', {
                'form': ReservaForm,
                'error': 'Error al registrar la reserva'
            })
            
def reserva_delete(request, id_reserva):
    reservar_habitacion = get_object_or_404(Reserva, pk=id_reserva)
    reservar_habitacion.delete()
    return redirect('listar_reservas')


def reservar_habitacion(request):
    return render(request, 'habitacionesReserva.html')