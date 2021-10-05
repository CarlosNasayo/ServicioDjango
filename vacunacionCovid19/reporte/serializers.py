from rest_framework import serializers
from reporte.models import Persona, Vacuna, Vacunacion

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields= ['id_persona','nombre','apellido','vacunado','fecha_nacimiento']

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields= ['id_vacuna','nombre','productor','cuantas_dosis']

class VacunacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacunacion
        fields= ['id_vacunacion','persona','vacuna','lugar_vacunacion','fecha_vacunacion','dosis','lote_vacuna']



