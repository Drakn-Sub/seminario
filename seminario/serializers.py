from rest_framework import serializers
from .models import Institucion, Inscrito

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ['id', 'nombre']
class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields =  ['id', 'nombre', 'institucion', 'nro_personas', 'telefono', 'fecha_inscripcion', 'hora_inscripcion', 'estado', 'observacion']
