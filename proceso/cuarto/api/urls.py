from proceso.cuarto.api.views import CuartoListView, CuartoDetailsView, CuartoDeleteView, CuartoUpdateView, \
    CuartoCreateView
from django.urls import path

urlpatterns = [
    path('list/', CuartoListView.as_view(), name='cuarto-list'),
    path('add/', CuartoCreateView.as_view(), name='cuarto-add'),
    path('update', CuartoUpdateView.as_view(), name='cuarto-add'),
    path('delete/', CuartoDeleteView.as_view(), name='cuarto-add'),
    path('details', CuartoDetailsView.as_view(), name='cuarto-add'),

]
