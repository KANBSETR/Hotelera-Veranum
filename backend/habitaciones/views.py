from django.shortcuts import render, redirect, get_object_or_404
from core.models import *
from django.http import JsonResponse, HttpResponseNotAllowed
import json

from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import HabitacionForm
from core.models import RegistroHabitacion



def listar_habitaciones(request):
    habitaciones = RegistroHabitacion.objects.all()
    return render(request, 'habitacion.html', {'habitaciones': habitaciones})

def habitacion_detail(request, id_habitacion):
    if request.method == 'GET':
        habitacion = get_object_or_404(RegistroHabitacion, pk=id_habitacion)
        form = HabitacionForm(instance=habitacion)
        return render(request, 'modificarHabitacion.html', {'habitacion': habitacion, 'form': form})
    else:
        try:
            habitacion = get_object_or_404(RegistroHabitacion, pk=id_habitacion)
            form = HabitacionForm(request.POST, instance=habitacion)
            form.save()
            return redirect('listar_habitaciones')
        except ValueError:
            return render(request, 'modificarHabitacion.html', {
                'habitacion': habitacion,
                'form': form,
                'error': 'Error al guardar la habitacion'
            })
              
def agregarHabitacion(request):
    if request.method == 'GET':
        return render(request, 'agregarHabitacion.html', {
            'form': HabitacionForm})
    else:
        try:
            form = HabitacionForm(request.POST)
            newHabitacion = form.save(commit=False)
            newHabitacion.user = request.user
            newHabitacion.save()
            return redirect('listar_habitaciones')
        except ValueError:
            return render(request, 'agregarHabitacion.html', {
                'form': HabitacionForm,
                'error': 'Error al guardar la casa'
            })
            

def habitacion_delete(request, id_habitacion):
    habitacion = get_object_or_404(RegistroHabitacion, pk=id_habitacion)
    habitacion.delete()
    return redirect('listar_habitaciones')

