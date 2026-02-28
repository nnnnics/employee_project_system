from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'assignments', views.EmployeeProjectViewSet)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('department/add/', views.add_department, name='add_department'),
    path('project/add/', views.add_project, name='add_project'),
    path('assign/', views.assign_employee, name='assign_employee'),
    path('employee/delete/<int:id>/', views.delete_employee, name='delete_employee'),
]