from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['nameDepartment', 'shortNameDepartment', 'activeDepartment']
        widgets = {
            'nameDepartment': forms.TextInput(attrs={
                'placeholder': 'Nombre del departamento'
            }),
            'shortNameDepartment': forms.TextInput(attrs={
                'placeholder': 'Sigla del departamento'
            }),
            'activeDepartment': forms.CheckboxInput(),
        }