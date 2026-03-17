from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from rest_framework import viewsets

from .models import Employer, Skills
from .forms import EmpleadoForm, SkillForm
from .serializers import EmployerSerializer, SkillSerializer


class ListarTodosLosEmpleados(ListView):
    template_name = 'employer/Listar_Todos_Los_Empleados.html'
    paginate_by = 2
    ordering = 'lastname'
    context_object_name = 'lista_empleados'
    model = Employer

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        return Employer.objects.filter(lastname__icontains=palabra_clave)


class ListarEmpleadosPorArea(ListView):
    template_name = 'employer/ListarEmpleadosPorArea.html'
    context_object_name = 'lista_empleados_por_area'
    model = Employer

    def get_queryset(self):
        area = self.kwargs.get('shortNameDepartment')
        return Employer.objects.filter(department__shortNameDepartment=area)


class AdministrarTodosLosEmpleados(ListView):
    template_name = 'employer/AdministrarTodosLosEmpleados.html'
    paginate_by = 2
    ordering = 'lastname'
    context_object_name = 'lista_empleados'
    model = Employer

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        return Employer.objects.filter(lastname__icontains=palabra_clave)


class CrearEmpleado(CreateView):
    model = Employer
    template_name = "employer/CrearEmpleado.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('employer_app:AdministrarTodosLosEmpleados')

    def form_valid(self, form):
        employer = form.save(commit=False)
        employer.fullname = f"{employer.name} {employer.lastname}"
        employer.save()
        form.save_m2m()
        return super().form_valid(form)


class ActualizarEmpleado(UpdateView):
    template_name = "employer/ActualizarEmpleado.html"
    context_object_name = 'ActualizarEmpleado'
    model = Employer
    form_class = EmpleadoForm
    success_url = reverse_lazy('employer_app:AdministrarTodosLosEmpleados')

    def form_valid(self, form):
        employer = form.save(commit=False)
        employer.fullname = f"{employer.name} {employer.lastname}"
        employer.save()
        form.save_m2m()
        return super().form_valid(form)


class EliminarEmpleado(DeleteView):
    model = Employer
    template_name = "employer/EliminarEmpleado.html"
    success_url = reverse_lazy('employer_app:AdministrarTodosLosEmpleados')


class DetallesDelEmpleado(DetailView):
    model = Employer
    template_name = 'employer/DetallesDelEmpleado.html'
    context_object_name = 'employerDetailView'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = self.object.skills.all()
        context['titulo'] = 'Empleado del mes'
        return context


class ListarHabilidades(ListView):
    model = Skills
    template_name = 'employer/ListarHabilidades.html'
    context_object_name = 'lista_habilidades'
    ordering = 'skill'


class CrearHabilidad(CreateView):
    model = Skills
    form_class = SkillForm
    template_name = 'employer/CrearHabilidad.html'
    success_url = reverse_lazy('employer_app:ListarHabilidades')


class ActualizarHabilidad(UpdateView):
    model = Skills
    form_class = SkillForm
    template_name = 'employer/ActualizarHabilidad.html'
    success_url = reverse_lazy('employer_app:ListarHabilidades')


class EliminarHabilidad(DeleteView):
    model = Skills
    template_name = 'employer/EliminarHabilidad.html'
    success_url = reverse_lazy('employer_app:ListarHabilidades')


class SuccesView(TemplateView):
    template_name = "employer/successView.html"


# API CRUD
class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.fullname = f"{obj.name} {obj.lastname}"
        obj.save()

    def perform_update(self, serializer):
        obj = serializer.save()
        obj.fullname = f"{obj.name} {obj.lastname}"
        obj.save()


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer