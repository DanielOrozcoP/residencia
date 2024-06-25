from rest_framework import generics
from proceso.dormitorio.api.serializers import DormitorioSerializer
from proceso.dormitorio.models import Dormitorio


# Create your views here.

class DormitorioListView(generics.ListAPIView):
    serializer_class = DormitorioSerializer

    def get_queryset(self):
        dormitorio = Dormitorio.objects.all()
        return dormitorio
