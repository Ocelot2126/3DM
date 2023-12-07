"""
URL configuration for mountains3dm project.

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
from django.urls import path
from mountains3dm.views import index,saludo,main,coordenadas,cambio3d,cargaarchivo,archivocargado,gracias,coordenadasenviadas,cambio3denviado 

app_name = 'mountains3dm'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'), # Lo que aparece primero es la direccion de la url, luego la funcion. Aca se llama igual
    path('main/', main, name='main'), # el html quedo como index.html
   # path('coordenadas/',coordenadas),
   path('coordenadas/', coordenadas, name='coordenadas'),
    path('cambio3d/',cambio3d, name='cambio3d'),
    path('cargaarchivo/',cargaarchivo, name='cargaarchivo'),
    path('archivocargado/',archivocargado, name='archivocargado'),
    path('gracias/',gracias, name='gracias'),
    path('coordenadasenviadas/',coordenadasenviadas, name='coordenadasenviadas'),
    path('cambio3denviado/',cambio3denviado, name='cambio3denviado'),
    path('', index, name='index'),  # Importando index desde .views
]

