from ctypes import create_unicode_buffer
from django.shortcuts import render

from .models import Ponente, Curso

# Create your views here.

def index(request):
    ponentes = Ponente.objects.all()
    return render(request, 'index.html', {'ponentes': ponentes})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'coneest/cursos/cursos.html', {'cursos': cursos})

def registro(request):
    return render(request, 'coneest/registro/registro.html')
