from rest_framework import serializers
from .models import Employee, Project, Department, EmployeeProject

class EmployeeSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Project.objects.all()
    )

    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'projects']

    def update(self, instance, validated_data):
        projects_data = validated_data.pop('projects', None)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if projects_data is not None:
            instance.projects.set(projects_data)

        return instance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProject
        fields = '__all__'