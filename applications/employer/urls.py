from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "employer_app"

router = DefaultRouter()
router.register(r'api/empleados', views.EmployerViewSet, basename='api-empleados')
router.register(r'api/habilidades', views.SkillViewSet, basename='api-habilidades')

urlpatterns = [
    path('empleados/', views.ListarTodosLosEmpleados.as_view(), name='ListarTodosLosEmpleados'),
    path('empleados/administrar/', views.AdministrarTodosLosEmpleados.as_view(), name='AdministrarTodosLosEmpleados'),
    path('empleados/crear/', views.CrearEmpleado.as_view(), name='CrearEmpleado'),
    path('empleados/editar/<int:pk>/', views.ActualizarEmpleado.as_view(), name='ActualizarEmpleado'),
    path('empleados/eliminar/<int:pk>/', views.EliminarEmpleado.as_view(), name='EliminarEmpleado'),
    path('empleados/detalle/<int:pk>/', views.DetallesDelEmpleado.as_view(), name='DetallesDelEmpleado'),

    path('habilidades/', views.ListarHabilidades.as_view(), name='ListarHabilidades'),
    path('habilidades/crear/', views.CrearHabilidad.as_view(), name='CrearHabilidad'),
    path('habilidades/editar/<int:pk>/', views.ActualizarHabilidad.as_view(), name='ActualizarHabilidad'),
    path('habilidades/eliminar/<int:pk>/', views.EliminarHabilidad.as_view(), name='EliminarHabilidad'),

    path('empleados/area/<str:shortNameDepartment>/', views.ListarEmpleadosPorArea.as_view(), name='ListarEmpleadosPorArea'),

    path('', include(router.urls)),
]