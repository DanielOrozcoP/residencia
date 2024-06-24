"""
URL configuration for Sigres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/estudiante/', include('proceso.estudiante.api.urls')),
    path('api/sede/', include('proceso.sede.api.urls')),
    path('api/cuarto/', include('proceso.cuarto.api.urls')),
    #path('api/dormitorio/', include('proceso.dormitorio.api.urls')),
    path('api/edificio/', include('proceso.edificio.api.urls')),
    #path('api/auth/', include('control_acceso.user_app.api.urls')),
]
