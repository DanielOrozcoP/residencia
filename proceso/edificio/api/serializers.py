from rest_framework import serializers
from proceso.dormitorio.api.serializers import DormitorioSerializer
from proceso.edificio.models import Edificio
#from proceso.sede.api.serializer import SedeSerializer


class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request', None)
        if request and 'edificio/' in request.path:
            dormitorios = DormitorioSerializer(instance.dormitorios, many=True, read_only=True).data
            representation['dormitorios'] = dormitorios
        return representation
