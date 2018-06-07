"""Proyecto0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# los frameworks web denominan a éste archivo de mapeo url routing
from django.contrib import admin  # viene por defecto
from django.urls import path  # viene por defecto
from django.conf.urls import url  #libreria antigua
from Aplicacion0.views import hola, inicio, saludo  # importamos la vista
# from Aplicacion0 import views   #otra forma

# Nuevas importaciones Use static() to add url mapping to serve static files during development (only)
# Django no sirve ficheros estáticos como CSS, JavaScript e imágenes por defecto, pero puede ser útil para el servidor
# web de desarrollo hacerlo así mientras creas tu sitio. Como adición final a este mapeador URL, puedes habilitar
# el servicio de ficheros estáticos durante el desarrollo añadiendo las líneas siguientes.

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # viene por defecto
    # url(r'^hola/',hola),  #formato antiguo este da error y además ya no se usa el arco circunflejo que da warning
    #path(r'^$', inicio, name='inicio'),
    #path(r'inicio', inicio),
    path(r'hola/', hola),  # forma nueva
    url(r'^$', inicio,name='inicio'),  # forma antigua lo coge sin poner inicio por defecto
    path(r'inicio/', inicio,name='inicio'),  # forma nueva lo coge colocando la palabra inicio
    path(r'saludo/', saludo,name='saludo'),  # forma nueva lo coge colocando la palabra saludo da error de formulario regform

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
