from rest_framework import serializers
from .models import Employer, Skills


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['id', 'skill']


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = [
            'id',
            'name',
            'lastname',
            'fullname',
            'job',
            'department',
            'skills',
            'cv',
            'avatar',
        ]