from django.db import models

class Ponente(models.Model):
    foto = models.ImageField(upload_to='ponentes/images')
    nombre_apellido = models.CharField(max_length=100)
    descripcion = models.TextField()
    universidad = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre_apellido

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion_curso = models.TextField()
    dia = models.DateField(auto_created=False, auto_now_add=False)
    hora = models.TimeField(auto_created=False, auto_now_add=False)
    ponente = models.ForeignKey(Ponente, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class MiniCurso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion_curso = models.TextField()
    dia = models.DateField(auto_created=False, auto_now_add=False)
    hora = models.TimeField(auto_created=False, auto_now_add=False)
    ponente = models.ForeignKey(Ponente, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre





