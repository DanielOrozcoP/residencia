from rest_framework import serializers
from proceso.edificio.api.serializers import EdificioSerializer
from proceso.sede.models import Sede


class SedeSerializer(serializers.ModelSerializer):
    edificios = EdificioSerializer(many=True, read_only=True)
    class Meta:
        model = Sede
        fields = (
            'id',
            'codigo',
            'direccion',
            'nombre',
            'edificios',
        )
