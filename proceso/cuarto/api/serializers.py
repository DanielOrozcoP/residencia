from rest_framework import serializers
from proceso.cuarto.models import Cuarto
from proceso.estudiante.api.serializers import EstudianteSerializers


class CuartoSerializer(serializers.ModelSerializer):
    estudiantes = EstudianteSerializers(many=True, read_only=True)

    class Meta:
        model = Cuarto
        fields = '__all__'

