from proceso.estudiante.api.views import EstudiantesListView, EstudianteCreateView, EstudianteDeleteView, \
    EstudianteUpdateView, EstudianteDetailsView
from django.urls import path

urlpatterns = [
    path('list/', EstudiantesListView.as_view(), name='estudiante-list'),
    path('add/', EstudianteCreateView.as_view(), name='estudiante-add'),
    path('update', EstudianteUpdateView.as_view(), name='estudiante-add'),
    path('delete/', EstudianteDeleteView.as_view(), name='estudiante-add'),
    path('details', EstudianteDetailsView.as_view(), name='estudiante-add'),
    # /api/estudiante/details?carnet_identidad={value}
    # /api/estudiante/delete?carnet_identidad={value}
    # /api/estudiante/update?carnet_identidad={value}
    # /api/estudiante/list/?{params}={value}&{params}={value}
]
