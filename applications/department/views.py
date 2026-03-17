from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .models import Department
from .forms import DepartmentForm
from .serializers import DepartmentSerializer

from pathlib import Path
import ast
import re
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms_settings import LocalSettingsForm

class IndexView(TemplateView):
    template_name = 'index.html'


class ApiHomeView(TemplateView):
    template_name = 'api_home.html'


class ListarDepartamentos(ListView):
    model = Department
    template_name = "department/ListarDepartamentos.html"
    context_object_name = 'lista_departamentos'
    ordering = ['nameDepartment']


class CrearDepartamento(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/CrearDepartamento.html'
    success_url = reverse_lazy('department_app:ListarDepartamentos')


class ActualizarDepartamento(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/ActualizarDepartamento.html'
    success_url = reverse_lazy('department_app:ListarDepartamentos')


class EliminarDepartamento(DeleteView):
    model = Department
    template_name = 'department/EliminarDepartamento.html'
    success_url = reverse_lazy('department_app:ListarDepartamentos')


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

def editar_local_settings(request):
    settings_path = Path(__file__).resolve().parent.parent.parent / 'empleado' / 'settings' / 'local.py'

    if not settings_path.exists():
        return render(request, 'settings_config/error.html', {
            'mensaje': f'No se encontró el archivo: {settings_path}'
        })

    content = settings_path.read_text(encoding='utf-8')

    allowed_hosts_match = re.search(r"ALLOWED_HOSTS\s*=\s*(\[[^\]]*\])", content, re.DOTALL)
    database_match = re.search(
        r"DATABASES\s*=\s*\{\s*'default'\s*:\s*\{(.*?)\}\s*\}",
        content,
        re.DOTALL
    )

    initial = {
        'allowed_hosts': '',
        'db_name': '',
        'db_user': '',
        'db_password': '',
        'db_port': '',
        'db_host': '',
    }

    if allowed_hosts_match:
        try:
            allowed_hosts = ast.literal_eval(allowed_hosts_match.group(1))
            initial['allowed_hosts'] = ",".join(allowed_hosts)
        except Exception:
            pass

    if database_match:
        block = database_match.group(1)

        def extract_value(key):
            match = re.search(rf"'{key}'\s*:\s*'([^']*)'", block)
            return match.group(1) if match else ''

        initial['db_name'] = extract_value('NAME')
        initial['db_user'] = extract_value('USER')
        initial['db_password'] = extract_value('PASSWORD')
        initial['db_port'] = extract_value('PORT')
        initial['db_host'] = extract_value('HOST')

    if request.method == 'POST':
        form = LocalSettingsForm(request.POST)
        if form.is_valid():
            allowed_hosts_list = [
                host.strip() for host in form.cleaned_data['allowed_hosts'].split(',')
                if host.strip()
            ]

            new_allowed_hosts = f"ALLOWED_HOSTS = {allowed_hosts_list}"

            new_databases = f"""DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{form.cleaned_data['db_name']}',
        'USER': '{form.cleaned_data['db_user']}',
        'PASSWORD': '{form.cleaned_data['db_password']}',
        'PORT': '{form.cleaned_data['db_port']}',
        'HOST': '{form.cleaned_data['db_host']}'
    }}
}}"""

            content_updated = re.sub(
                r"ALLOWED_HOSTS\s*=\s*\[[^\]]*\]",
                new_allowed_hosts,
                content,
                flags=re.DOTALL
            )

            content_updated = re.sub(
                r"DATABASES\s*=\s*\{\s*'default'\s*:\s*\{.*?\}\s*\}",
                new_databases,
                content_updated,
                flags=re.DOTALL
            )

            settings_path.write_text(content_updated, encoding='utf-8')
            messages.success(request, 'Archivo local.py actualizado correctamente.')
            return redirect('department_app:editar_local_settings')
    else:
        form = LocalSettingsForm(initial=initial)

    return render(request, 'settings_config/editar_local_settings.html', {
        'form': form
    })