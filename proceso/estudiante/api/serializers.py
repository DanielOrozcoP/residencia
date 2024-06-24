from rest_framework import serializers
from proceso.estudiante.api.helpers import ci_date
from proceso.cuarto.models import Cuarto
from proceso.estudiante.models import Estudiante


class EstudianteSerializers(serializers.ModelSerializer):
    cuarto = serializers.SlugRelatedField(
        slug_field='codigo',
        queryset=Cuarto.objects.all()
    )

    class Meta:
        model = Estudiante
        fields = [
            'id', 'carnet_identidad',
            'nombre', 'apellido',
            'facultad', 'carrera',
            'ano_academico', 'eliminado',
            'cuarto',
        ]

    def validate_carnet_identidad(self, value):
        if len(value) != 11:
            raise serializers.ValidationError(
                'Error'
            )
        else:
            if not ci_date(value):
                raise serializers.ValidationError(
                    'La fecha de nacimiento proporcionada en el carnet de identidad no es correcta.'
                )
            else:
                return value

    def validate_ano_academico(self, value):
        if 1 <= value <= 5:
            return value
        else:
            raise serializers.ValidationError(
                F'Ninguna carrera tiene esta cantidad: {value} de años academicos.'
            )
