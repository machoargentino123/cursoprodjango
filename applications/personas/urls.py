from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
    print("<html>-----------------------Hola mundo/ desde APP personas--------------------------</html>")

app_name = 'persona_app'

urlpatterns = [
     #muestra codigo en la consola
    #agregaremos para que acada app tenga su propio archivo URL.#
   
#------------------------------------aca empieza el proyecto -----------------------------------    
     #pagina de inicio Templateview
    path('', views.InicioView.as_view(), name = 'inicio'),
    #listar todos los empleados listview
    path('listar_empleados/', views.ListAllEmpleados.as_view(), name='Empleados_all'),
    #listar empleados por area se llega desde la pagina de departamentos. Listview
    path('listar_area/<shorname>', views.ListByAreaEmpleados.as_view(), name='empleado_area'),
    #ver empleado detallado detailview
    path('verempleado2/<pk>', views.EmpleadoDetailView2.as_view(),name = 'empleado_detail'),
    #administrar empleados listview
    path('administrar/', views.AdminisitrarEmpleados.as_view(), name='administrar'),
    #Actualizar empleados updateview
    path('update/<pk>', views.EmpleadoUpdateView.as_view(), name = 'actualizar'),
    #borrar empleado deleteview
    path('delete/<pk>', views.EmpleadoDeleteView.as_view(), name = 'delete'),
    #agregar empleado
    path('add_empleado/', views.AddEmpleados.as_view(), name = 'add_empleado'),
#----------------------------------- aca etrmina el projecto son todos ejemplos -----------------
    path('listar_area2/', views.ListByJob.as_view()),
    path('listar_area3/<shortname>/', views.ListByURL.as_view()),
    path('buscarempleado/', views.ListByKeyword.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('verempleado/<pk>', views.EmpleadoDetailView.as_view()), #detailed view, usa el pk un registro
    path('addempleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessCreateView.as_view(), name = 'correcto'),
    path('addempleado2/', views.EmpleadoCreateView2.as_view()),
    path('success2/', views.SuccessCreateView2.as_view(), name = 'correcto2'),
    path('success3/', views.SuccessCreateView3.as_view(), name = 'correcto3'),
    path('delete/<pk>', views.EmpleadoDeleteView.as_view(), name = 'delete'),
    path('personas/', DesdeApps),

]
