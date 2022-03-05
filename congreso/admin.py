from django.contrib import admin

from .models import Ponente, Curso, MiniCurso



# Register your models here.

admin.site.register(Ponente)
admin.site.register(Curso)
admin.site.register(MiniCurso)
