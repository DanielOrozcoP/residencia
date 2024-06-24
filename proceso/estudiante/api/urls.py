from proceso.estudiante.api.views import EstudiantesListView, EstudianteCreateView, EstudianteDeleteView, \
    EstudianteUpdateView, EstudianteDetailsView
from django.urls import path



urlpatterns = [
    path('list/', EstudiantesListView.as_view(), name='estudiante-list'),
    path('add/', EstudianteCreateView.as_view(), name='estudiante-add'),
    # hay que ponerle el parametro "id" en el postam
    path('update/', EstudianteUpdateView.as_view(), name='estudiante-add'),
    path('delete/', EstudianteDeleteView.as_view(), name='estudiante-add'),
    path('details/', EstudianteDetailsView.as_view(), name='estudiante-add'),
]
