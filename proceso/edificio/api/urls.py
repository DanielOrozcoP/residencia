from proceso.edificio.api.views import *
from django.urls import path

urlpatterns = [
    path('list/', EdificioListView.as_view(), name='edificio-list'),
    path('add/', EdificioCreateView.as_view(), name='edificio-add'),
    path('update/', EdificioUpdateView.as_view(), name='edificio-update'),  # hay que ponerle el parametro "id" en el postam
    path('details/', EdificioDetailsView.as_view(), name='edificio-details'),  # Hay que ponerle el parametro "id" en el postam
    path('delete/', EdificioDeleteView.as_view(), name='edificio-delete'),  # Hay que ponerle el parametro "id" en el postam
]