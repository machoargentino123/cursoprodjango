from django.contrib import admin
from django.urls import path

from . import views

def DesdeApps(self):
    print("-----------------------Hola mundo/ desde APP departamento--------------------------")

app_name = 'departamento_app'

urlpatterns = [
    path('departamentos/', views.DepartamentoListView.as_view(), name= 'departamentos'),
    path('newdepartamento/', views.NewdepartamentoView.as_view(), name= 'newdepartamento'),
    
    
]
