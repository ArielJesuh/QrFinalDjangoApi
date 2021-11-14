from .models import *
from rest_framework import serializers

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ["id","usuario","password","asignatura"]

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ["id","alumno","clase"]

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ["id","usuario","password"]

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ["id","nombre","curso"]

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ["id","hora","curso"]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["id","seccion","asignatura"]
        
