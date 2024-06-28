from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import PersonaForm, EmpleadoForm, UsuarioForm
from core.models import Persona
import json
from django.http import JsonResponse
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from .models import Empleado, Usuario

def inicio(request):
    return render(request, 'inicio.html')

def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'formularioLogin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'formularioLogin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })


    
    
def formulario (request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonaForm()
    return render(request, 'registro.html', {'form': form})



def register(request):
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        employee_form = EmpleadoForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if persona_form.is_valid():
            user = persona_form.save()
            form_type = request.POST.get('form_type')
            if form_type == 'employee':
                employee_form = EmpleadoForm(request.POST)
                if employee_form.is_valid():
                    employee = employee_form.save(commit=False)
                    employee.rut = user.rut
                    employee.save()
                else:
                    messages.error(request, 'Formulario de empleado no válido')
                    return render(request, 'registro.html', {'persona_form': persona_form, 'employee_form': employee_form})
            elif form_type == 'user':
                usuario_form = UsuarioForm(request.POST)
                if usuario_form.is_valid():
                    usuario = usuario_form.save(commit=False)
                    usuario.rut = user.rut
                    usuario.save()
                else:
                    messages.error(request, 'Formulario de usuario no válido')
                    return render(request, 'registro.html', {'persona_form': persona_form, 'usuario_form': usuario_form})
            return redirect('base.html')
        else:
            messages.error(request, 'Formulario de persona no válido')
    else:
        persona_form = PersonaForm()
        employee_form = EmpleadoForm()
        usuario_form = UsuarioForm()
    return render(request, 'registro.html', {'persona_form': persona_form, 'employee_form': employee_form, 'usuario_form': usuario_form})

def about(request):
    return render(request, 'about.html')

def usuario(request):
    return render(request, 'usuarios.html')