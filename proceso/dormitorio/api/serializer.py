from rest_framework import serializers
from proceso.dormitorio.models import Dormitorio
from proceso.edificio.api.serializer import EdificioSerializer


class DormitorioSerializer(serializers.ModelSerializer):
    edificioID = EdificioSerializer(read_only=True)

    class Meta:
        model = Dormitorio
        fields = (
            'id',
            'nombre',
            'apellidos',
            'edificioID'
        )
