from proceso.dormitorio.api.views import DormitorioListView
from django.urls import path

urlpatterns = [
    path('list/', DormitorioListView.as_view(), name='dormitorio-list'),
]
