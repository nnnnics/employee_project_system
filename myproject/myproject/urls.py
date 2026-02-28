from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from management import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'assignments', views.EmployeeProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('management.urls')),
    path('api/', include(router.urls)),
]