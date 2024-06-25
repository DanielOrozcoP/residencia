from rest_framework import serializers
from proceso.cuarto.api.serializers import CuartoSerializer
from proceso.dormitorio.models import Dormitorio


class DormitorioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dormitorio
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request', None)
        if request and 'dormitorio/' in request.path:
            cuartos = CuartoSerializer(instance.cuartos, many=True, read_only=True).data
            representation['cuartos'] = cuartos
        return representation
