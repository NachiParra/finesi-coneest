from ctypes import create_unicode_buffer
from django.shortcuts import render

from .models import Ponente, Curso, MiniCurso

# Create your views here.

def index(request):
    ponentes = Ponente.objects.all()
    cursos = Curso.objects.all()
    mini_cursos = MiniCurso.objects.all()
    return render(request, 'index.html', {'ponentes': ponentes, 'cursos': cursos, 'mini_cursos': mini_cursos})

def cursos(request):
    cursos = Curso.objects.all()
    mini_cursos= MiniCurso.objects.all()
    return render(request, 'coneest/cursos/cursos.html', {'cursos': cursos, 'mini_cursos': mini_cursos})

def registro(request):
    return render(request, 'coneest/registro/registro.html')

def cronograma(request):
    return render(request, 'coneest/cronograma/cronograma.html')
