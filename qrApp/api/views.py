from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

#Viewsets del alumno
class AlumnoViewSet(generics.ListAPIView): # Lista de un Alumno
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoBuscarViewSet(generics.ListAPIView): # Lista de todos los Alumnos
    serializer_class = AlumnoSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Alumno.objects.filter(id=laid)
#Viewsets del alumno

#Viewsets del profesor
class ProfesorViewSet(generics.ListAPIView): # Lista de todos los Profesores
    serializer_class = ProfesorSerializer
    queryset = Profesor.objects.all()

class ProfesorBuscarViewSet(generics.ListAPIView): # Lista de un Profesor
    serializer_class = ProfesorSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Profesor.objects.filter(id=laid)
#Viewsets del profesor

#Viewsets del curso
class CursoViewSet(generics.ListAPIView): # Lista de todos los Cursos
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class CursoBuscarViewSet(generics.ListAPIView): # Lista de un Curso
    serializer_class = CursoSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Curso.objects.filter(id=laid)
#Viewsets del curso

#Viewsets de la asistencia
class AsistenciaViewSet(generics.ListAPIView): # Lista de todas las Asistencias
    serializer_class = AsistenciaSerializer
    queryset = Asistencia.objects.all()

class AsistenciaBuscarViewSet(generics.ListAPIView): # Lista de una Asistencia
    serializer_class = AsistenciaSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Asistencia.objects.filter(id=laid)
#Viewsets de la asistencia

#Viewsets de la Asignatura
class AsignaturaViewSet(generics.ListAPIView): # Lista de todas las Asignaturas
    serializer_class = AsignaturaSerializer
    queryset = Asignatura.objects.all()

class AsignaturaBuscarViewSet(generics.ListAPIView): # Lista de una Asignatura
    serializer_class = AsignaturaSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Asignatura.objects.filter(id=laid)
#Viewsets de la Asignatura

#Viewsets de la Clase
class ClaseViewSet(generics.ListAPIView): # Lista de todas las Clases
    serializer_class = ClaseSerializer
    queryset = Clase.objects.all()

class ClaseBuscarViewSet(generics.ListAPIView): # Lista de una Clase
    serializer_class = ClaseSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Clase.objects.filter(id=laid)
#Viewsets de la Clase

#Viewsets de la Curso
class CursoViewSet(generics.ListAPIView): # Lista de todos los Cursos
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class CursoBuscarViewSet(generics.ListAPIView): # Lista de un Curso
    serializer_class = CursoSerializer
    def get_queryset(selft):
        laid = selft.kwargs['id']
        return Curso.objects.filter(id=laid)
#Viewsets de la Curso