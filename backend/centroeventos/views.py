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


from core.models import Eventos

def eventos(request):
    return render(request, 'evento.html')

from .forms import EventosForm
from core.models import Eventos



def listar_eventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'evento.html', {'eventos': eventos})




def evento_detail(request, idEvento):
    if request.method == 'GET':
        eventos = get_object_or_404(Eventos, pk=idEvento)
        form = EventosForm(instance=eventos)
        return render(request, 'modificarEvento.html', {'eventos': eventos, 'form': form})
    else:
        try:
            eventos = get_object_or_404(Eventos, pk=idEvento)
            form = EventosForm(request.POST, instance=eventos)
            form.save()
            return redirect('listar_eventos')
        except ValueError:
            return render(request, 'modificarEvento.html', {
                'servicio': eventos,
                'form': form,
                'error': 'Error al guardar el evento'
            })
            
            
            
def agregarEvento(request):
    if request.method == 'GET':
        return render(request, 'agregarEvento.html', {
            'form': EventosForm})
    else:
        try:
            form = EventosForm(request.POST)
            newEvento = form.save(commit=False)
            newEvento.user = request.user
            newEvento.save()
            return redirect('listar_eventos')
        except ValueError:
            return render(request, 'agregarEvento.html', {
                'form': EventosForm,
                'error': 'Error al guardar el evento'
            })
            



def evento_delete(request, idEvento):
    evento = get_object_or_404(Eventos, pk=idEvento)
    evento.delete()
    return redirect('listar_eventos')

