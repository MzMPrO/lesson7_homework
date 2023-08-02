from django.contrib import admin
from django.conf.urls import static
from django.urls import path, include

from lesson7_homework import settings

urlpatterns = [
    path('', include('branch.urls')),
    path('', include('department.urls')),
    path('', include('employee.urls')),
    path('', include('profession.urls')),
    path('admin/', admin.site.urls),
]
