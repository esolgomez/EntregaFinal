# from django.http import HttpResponse
from datetime import datetime
# from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random

from Home.models import Humano

def crear_persona(request, nombre, apellido):
    persona = Humano(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_creacion=datetime.now())
    persona.save()
    return render(request, 'Home/crear_persona.html', {'persona': persona})

def ver_personas(request):
    personas = Humano.objects.all()
    return render(request, 'Home/ver_personas.html')

def index(request):
    return render(request, 'Home/index.html')
