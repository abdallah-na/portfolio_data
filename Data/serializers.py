from django.db.models import fields
from rest_framework import serializers
from .models import *

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        module = AboutMe
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        models = Education
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        models = Work
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        models = Project
        fields = '__all__'

