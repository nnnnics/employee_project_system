from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Project, Department, EmployeeProject
from .forms import EmployeeForm, ProjectForm, DepartmentForm, EmployeeProjectForm

# READ (Dashboard)
def dashboard(request):
    employees = Employee.objects.all()
    projects = Project.objects.all()
    departments = Department.objects.all()
    assignments = EmployeeProject.objects.all()

    return render(request, 'dashboard.html', {
        'employees': employees,
        'projects': projects,
        'departments': departments,
        'assignments': assignments
    })

# CREATE
def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form, 'title': 'Add Employee'})

def add_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form, 'title': 'Add Department'})

def add_project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form, 'title': 'Add Project'})

def assign_employee(request):
    form = EmployeeProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form, 'title': 'Assign Employee to Project'})

# DELETE
def delete_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('dashboard')

#DRF
from rest_framework import viewsets
from .serializers import EmployeeSerializer, DepartmentSerializer, ProjectSerializer, EmployeeProjectSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EmployeeProjectViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProject.objects.all()
    serializer_class = EmployeeProjectSerializer