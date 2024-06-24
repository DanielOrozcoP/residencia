from rest_framework import generics
from proceso.cuarto.api.serializers import CuartoSerializer
from proceso.cuarto.models import Cuarto


# Create your views here.

class ListCuarto(generics.ListAPIView):
    serializer_class = CuartoSerializer

    def get_queryset(self):
        cuarto = Cuarto.objects.all()
        return cuarto
