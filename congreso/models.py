from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion_curso = models.TextField()
    dia = models.DateField(auto_created=False, auto_now_add=False)
    hora = models.TimeField(auto_created=False, auto_now_add=False)

    def __str__(self):
        return self.nombre

class MiniCurso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion_curso = models.TextField()
    dia = models.DateField(auto_created=False, auto_now_add=False)
    hora = models.TimeField(auto_created=False, auto_now_add=False)

    def __str__(self):
        return self.nombre



class Ponente(models.Model):
    foto = models.ImageField(upload_to='ponentes/images')
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    descripcion = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    minicurso = models.ForeignKey(MiniCurso, on_delete=models.CASCADE, null=True)
    universidad = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)


    def __str__(self):
        return self.nombres


