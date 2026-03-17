from django import forms
from .models import Employer, Skills


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('name', 'lastname', 'job', 'department', 'cv', 'avatar', 'fullname', 'skills')
        widgets = {
            'skills': forms.CheckboxSelectMultiple()
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']
        widgets = {
            'skill': forms.TextInput(attrs={
                'placeholder': 'Ingrese la habilidad'
            })
        }