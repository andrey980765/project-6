# core/serializers.py
from rest_framework import serializers
from .models import Client, Project, Building, Contractor

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
        read_only_fields = ('created_at',)

class ProjectSerializer(serializers.ModelSerializer):
    buildings = BuildingSerializer(many=True, read_only=True)
    contractors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'

class ContractorSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all(), required=False)
    class Meta:
        model = Contractor
        fields = '__all__'
