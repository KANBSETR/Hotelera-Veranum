from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
import json

from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from core.models import HotelDetalle
from .forms import InventarioForm


def inventario(request):
    return render(request, 'inventario.html')

def listar_inventario(request):
    inventarios = HotelDetalle.objects.all()
    return render(request, 'inventario.html', {'inventarios': inventarios})

def inventario_detail(request, id_inventario):
    if request.method == 'GET':
        inventarios = get_object_or_404(HotelDetalle, pk=id_inventario)
        form = InventarioForm(instance=inventarios)
        return render(request, 'modificarInventario.html', {'inventarios': inventarios, 'form': form})
    else:
        try:
            inventarios = get_object_or_404(HotelDetalle, pk=id_inventario)
            form = InventarioForm(request.POST, instance=inventarios)
            form.save()
            return redirect('listar_inventario')
        except ValueError:
            return render(request, 'modificarInventario.html', {
                'inventarios': inventarios,
                'form': form,
                'error': 'Error al guardar el inventario'
            })
              
def agregarInventario(request):
    if request.method == 'GET':
        return render(request, 'agregarInventario.html', {
            'form': InventarioForm})
    else:
        try:
            form = InventarioForm(request.POST)
            newInventario = form.save(commit=False)
            newInventario.user = request.user
            newInventario.save()
            return redirect('listar_inventario')
        except ValueError:
            return render(request, 'agregarInventario.html', {
                'form': InventarioForm,
                'error': 'Error al guardar el inventario'
            })
            

def inventario_delete(request, id_inventario):
    inventarios = get_object_or_404(HotelDetalle, pk=id_inventario)
    inventarios.delete()
    return redirect('listar_inventario')



