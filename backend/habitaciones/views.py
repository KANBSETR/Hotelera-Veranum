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

"""
def registrar_habitacion(request):
    if request.method == 'POST':
        numero_habitacion = request.POST.get('numero_habitacion')
        cant_dormitorios = request.POST.get('cant_dormitorios')
        cant_banos = request.POST.get('cant_banos')
        cant_camas = request.POST.get('cant_camas')
        tamano_camas = request.POST.get('tamano_camas')
        cant_personas_disp = request.POST.get('cant_personas_disp')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        estado_habitacion = request.POST.get('estado_habitacion')
        id_servicio = request.POST.get('id_servicio')
        id_tipo_habitacion = request.POST.get('id_tipo_habitacion')
        id_empleado = request.POST.get('id_empleado')
        id_hotel = request.POST.get('id_hotel')
        habitacion = RegistroHabitacion(
            numero_habitacion=numero_habitacion,
            cant_dormitorios=cant_dormitorios,
            cant_banos=cant_banos,
            cant_camas=cant_camas,
            tamano_camas=tamano_camas,
            cant_personas_disp=cant_personas_disp,
            descripcion=descripcion,
            precio=precio,
            estado_habitacion=estado_habitacion,
            id_servicio=id_servicio,
            id_tipo_habitacion=id_tipo_habitacion,
            id_empleado=id_empleado,
            id_hotel=id_hotel

        )
        habitacion.save()
        messages.success(
            request, f"La habitacion con id: {id} fue registrado correctamente...")
        return redirect('listar_habitaciones')
    return redirect('inicio')
    
    def eliminar_habitacion(request):
    if request.method != 'DELETE':
        return HttpResponseNotAllowed(['DELETE'])
    try:
        id = json.loads(request.body)['id']
        habitacion = RegistroHabitacion.objects.get(id=id)
        habitacion.delete()
        return JsonResponse({'resultado': 'Habitacion eliminada con éxito.'})
    except ObjectDoesNotExist:
        return JsonResponse({'resultado': 'Habitacion no encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'resultado': f'Error al eliminar la habitacion: {str(e)}'}, status=500)
        

def actualizar_habitacion(request, id):
    try:
        if request.method == "POST":
            habitacion = RegistroHabitacion.objects.get(id=id)
            
            numero_habitacion = request.POST.get('numero_habitacion')
            cant_dormitorios = request.POST.get('cant_dormitorios')
            cant_banos = request.POST.get('cant_banos')
            cant_camas = request.POST.get('cant_camas')
            tamano_camas = request.POST.get('tamano_camas')
            cant_personas_disp = request.POST.get('cant_personas_disp')
            descripcion = request.POST.get('descripcion')
            precio = request.POST.get('precio')
            estado_habitacion = request.POST.get('estado_habitacion')
            id_servicio = request.POST.get('id_servicio')
            id_tipo_habitacion = request.POST.get('id_tipo_habitacion')
            id_empleado = request.POST.get('id_empleado')
            id_hotel = request.POST.get('id_hotel')
            habitacion.save()
        return redirect('listar_habitaciones')
    
    except ObjectDoesNotExist:
        error_message = f"La habitacion con id: {id} no se actualizó."
        return render(request, "habitaciones/lista_habitacion.html", {"error_message": error_message})
    

"""
