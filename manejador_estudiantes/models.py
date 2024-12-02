from django.db import models

class Colegio(models.Model):
    nombre =  models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.nombre)

class Estudiante(models.Model):
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    nombre =  models.CharField(max_length=50)
    documento = models.CharField(max_length=50)
    curso = models.CharField(max_length=15)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return str(self.nombre)