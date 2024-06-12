from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError



def formulario(request):
    return render(request, 'formularioRegistro.html')



def inicio(request):
    return render(request, 'inicio.html')




def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'formularioLogin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, nombre_usuario=request.POST['nombre_usuario'],
                            contrasena=request.POST['contrasena'])
        if user is None:
            return render(request, 'formularioLogin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('habitaciones')


def signup(request):
    if request.method == 'GET':
        return render(request, 'formularioRegistro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['contrasena']:
            try:
                user = User.objects.create_user(username=request.POST['nombre_usuario'],
                                                password=request.POST['contrasena'])
                user.save()
                login(request, user)
                return redirect('base')
            except IntegrityError:
                return render(request, 'formularioRegistro.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario ya existe'
                })
        return render(request, 'formularioRegistro.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

