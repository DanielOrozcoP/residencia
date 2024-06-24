from rest_framework import serializers
from proceso.edificio.models import Edificio
#from proceso.sede.api.serializer import SedeSerializer


class EdificioSerializer(serializers.ModelSerializer):
    #sedeID = SedeSerializer(read_only=True)

    class Meta:
        model = Edificio
        fields = [
            'id',
            'codigo',
            'sexo',
            #'sedeID',
        ]
