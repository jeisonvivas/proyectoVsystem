from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):
    
    estudiante = Persona.objects.filter(rol='Estudiante')
    # select * from persona where rol = 'Estudiante'
    
    
    return render(request,'Lista-estudiantes.html',{
        'title' : 'Lista de estudiantes',
        'estudiantes': estudiante
    })
