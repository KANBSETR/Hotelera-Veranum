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