from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso.sede.models import Sede
from proceso.sede.api.serializer import SedeSerializer


# Create your views here.

class SedeCreateView(generics.CreateAPIView):
    serializer_class = SedeSerializer

    def perform_create(self, serializer):
        serializer.save()


class SedeUpdateView(generics.UpdateAPIView):
    serializer_class = SedeSerializer

    def get_object(self):  # Sobreescribir el metodo get_object()
        queryset = Sede.objects.all()  # Consulta
        sede = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return sede


class SedeDetailsView(generics.RetrieveAPIView):
    serializer_class = SedeSerializer

    def get_object(self):
        queryset = Sede.objects.all()
        sede = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return sede


class SedeDeleteView(generics.DestroyAPIView):
    serializer_class = SedeSerializer

    def get_object(self):
        queryset = Sede.objects.all()
        sede = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return sede


class SedeListView(generics.ListAPIView):
    serializer_class = SedeSerializer

    def get_queryset(self):
        sede = Sede.objects.all()
        return sede
