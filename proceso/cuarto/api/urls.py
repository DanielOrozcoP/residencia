from proceso.cuarto.api.views import ListCuarto
from django.urls import path

urlpatterns = [
    path('list/', ListCuarto.as_view(), name='cuarto-list'),
]
