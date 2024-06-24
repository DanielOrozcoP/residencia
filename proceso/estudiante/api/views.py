from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from proceso.estudiante.api.serializers import EstudianteSerializers
from proceso.estudiante.models import Estudiante


# Create your views here.


class EstudianteCreateView(generics.CreateAPIView):  # Clase para crear un nuevo estudiante
    serializer_class = EstudianteSerializers  # Define el serializer que se utilizará

    def perform_create(self, serializer):  # Método que se llama al crear un nuevo objeto
        # pk = self.kwargs['pk']  # Obtiene el ID (clave primaria) del estudiante desde los argumentos de la URL
        # estudiante = Estudiante.objects.get(pk=pk)  # Busca el estudiante en la base de datos usando la clave primaria
        serializer = EstudianteSerializers(data=self.request.data)
        if serializer.is_valid():
            serializer.save()  # Guarda el nuevo objeto asociado al estudiante encontrado


class EstudiantesListView(generics.ListAPIView):  # Clase para obtener una lista de estudiantes
    serializer_class = EstudianteSerializers  # Define el serializer que se utilizará

    def get_queryset(self):  # Método que retorna el queryset de objetos a listar
        estudiante = Estudiante.objects.all()  # Obtiene todos los estudiantes de la base de datos
        return estudiante.filter(
            eliminado=False)  # Filtra los estudiantes para excluir los que tienen 'eliminado' como True


class EstudianteUpdateView(generics.UpdateAPIView):
    serializer_class = EstudianteSerializers

    def get_object(self):  # Sobreescribir el metodo get_object()
        queryset = Estudiante.objects.filter(eliminado=False)  # Consulta
        estudiante = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return estudiante


class EstudianteDetailsView(generics.RetrieveAPIView):
    serializer_class = EstudianteSerializers

    def get_object(self):
        queryset = Estudiante.objects.filter(eliminado=False)
        estudiante = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return estudiante


class EstudianteDeleteView(generics.DestroyAPIView):
    serializer_class = EstudianteSerializers

    def get_object(self):
        queryset = Estudiante.objects.filter(eliminado=False)
        estudiante = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return estudiante
