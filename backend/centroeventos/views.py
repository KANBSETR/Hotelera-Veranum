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
from .forms import CentroEventosForm
from core.models import Eventos



def listar_servicios(request):
    servicioAd = RegistroServicioAdicional.objects.all()
    return render(request, 'servicioAd.html', {'servicioAd': servicioAd})




def servicio_detail(request, id_servicio):
    if request.method == 'GET':
        servicioAd = get_object_or_404(RegistroServicioAdicional, pk=id_servicio)
        form = ServicioAdForm(instance=servicioAd)
        return render(request, 'modificarServicio.html', {'servicioaAd': servicioAd, 'form': form})
    else:
        try:
            servicioAd = get_object_or_404(RegistroServicioAdicional, pk=id_servicio)
            form = ServicioAdForm(request.POST, instance=servicioAd)
            form.save()
            return redirect('listar_servicios')
        except ValueError:
            return render(request, 'modificarServicio.html', {
                'servicio': servicioAd,
                'form': form,
                'error': 'Error al guardar el servicio adicional'
            })
            
            
            
def agregarServicio(request):
    if request.method == 'GET':
        return render(request, 'agregarServicio.html', {
            'form': ServicioAdForm})
    else:
        try:
            form = ServicioAdForm(request.POST)
            newServicioAd = form.save(commit=False)
            newServicioAd.user = request.user
            newServicioAd.save()
            return redirect('listar_servicios')
        except ValueError:
            return render(request, 'agregarServicio.html', {
                'form': ServicioAdForm,
                'error': 'Error al guardar el servicio adicional'
            })
            



def servicio_delete(request, id_servicio):
    servicioAd = get_object_or_404(RegistroServicioAdicional, pk=id_servicio)
    servicioAd.delete()
    return redirect('listar_servicios')
