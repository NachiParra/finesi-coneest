from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre



class Ponente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    universidad = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='ponentes/images')
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombres



