from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "department_app"

router = DefaultRouter()
router.register(r'api/departamentos', views.DepartmentViewSet, basename='api-departamentos')

urlpatterns = [
    path('departamentos/', views.ListarDepartamentos.as_view(), name='ListarDepartamentos'),
    path('departamentos/crear/', views.CrearDepartamento.as_view(), name='CrearDepartamento'),
    path('departamentos/editar/<int:pk>/', views.ActualizarDepartamento.as_view(), name='ActualizarDepartamento'),
    path('departamentos/eliminar/<int:pk>/', views.EliminarDepartamento.as_view(), name='EliminarDepartamento'),

    path('api/', views.ApiHomeView.as_view(), name='api_home'),
     path('configuracion/local/', views.editar_local_settings, name='editar_local_settings'),
    path('', include(router.urls)),
]