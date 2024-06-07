from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError



def formulario(request):
    return render(request, 'formularioRegistro.html')

def inicioSesion(request):
    return render(request, 'formularioLogin.html')

def inicio(request):
    return render(request, 'inicio.html')