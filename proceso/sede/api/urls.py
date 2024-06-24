from proceso.sede.api.views import SedeListView, SedeCreateView, SedeUpdateView, SedeDeleteView, SedeDetailsView
from django.urls import path

urlpatterns = [
    path('list/', SedeListView.as_view(), name='sede-list'),
    path('add/', SedeCreateView.as_view(), name='sede-add'),
    # hay que ponerle el parametro "id" en el postam
    path('update/', SedeUpdateView.as_view(), name='sede-update'),
    path('details/', SedeDetailsView.as_view(), name='sede-details'),
    path('delete/', SedeDeleteView.as_view(), name='sede-delete'),
]
