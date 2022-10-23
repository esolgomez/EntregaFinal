# from django.http import HttpResponse
from datetime import datetime
# from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random

from Home.models import Humano

def crear_persona(request):
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        persona = Humano(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_creacion=datetime.now())
        persona.save()
        
        return redirect('ver_personas')
    
    return render(request, 'Home/crear_persona.html', {})

def ver_personas(request):
    personas = Humano.objects.all()
    return render(request, 'Home/ver_personas.html', {'personas': personas})

def index(request):
    return render(request, 'Home/index.html')
