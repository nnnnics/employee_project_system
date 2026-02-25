from django import forms
from .models import Employee, Project, Department, EmployeeProject

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'department']

class EmployeeProjectForm(forms.ModelForm):
    class Meta:
        model = EmployeeProject
        fields = ['employee', 'project']