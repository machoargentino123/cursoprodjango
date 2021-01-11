from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static #paquete que permite generar URL staticas

def PruebaUrl(self):
    print("-----------------------Hola mundo/ solop imprime en la consola--------------------------")


urlpatterns = [
    path('admin/', admin.site.urls),
    #agregaremos para que acada app tenga su propio archivo URL.#
    re_path('',include('applications.departamentos.urls')),
    re_path('',include('applications.personas.urls')),
    re_path('',include('applications.home.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
