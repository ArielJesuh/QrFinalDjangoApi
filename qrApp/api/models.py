from django.db import models

# Create your models here.

class Curso(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    seccion = models.CharField(max_length=50)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE,related_name='+',null=True,blank=True)
    def __str__(self):
        return self.id  

class Clase(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    hora = models.DateTimeField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE,related_name='+',null=True,blank=True)
    def __str__(self):
        return self.id

class Asignatura(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)
    curso = models.ManyToManyField(Curso,related_name='+',null=True,blank=True)
    def __str__(self):
        return self.id

class Alumno(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    asignatura = models.ManyToManyField(Asignatura)
    def __str__(self):
        return self.id

class Asistencia(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    def __str__(self):
        return self.id

class Profesor(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    curso = models.ManyToManyField(Curso,related_name='+',null=True,blank=True)

    def __str__(self):
        return self.id




    
