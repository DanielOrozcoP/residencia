from rest_framework import serializers
from proceso.cuarto.models import Cuarto


class CuartoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuarto
        fields = '__all__'

