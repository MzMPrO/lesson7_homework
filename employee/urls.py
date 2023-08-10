from django.urls import path

from employee import views
from employee.views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDetailsView
from department.views import login_required

urlpatterns = [
    path("employees/list/", login_required(EmployeeListView.as_view()), name="employees-list"),
    path("employees/create/", login_required(EmployeeCreateView.as_view()), name="employees-create"),
    path("employees/<int:pk>/update/", login_required(EmployeeUpdateView.as_view()), name="employees-Update"),
    path("employees/<int:pk>/detail/", login_required(EmployeeDetailsView.as_view()), name="employees-detail"),
    path("employees/<int:pk>/delete/", views.employee_delete, name="employees-delete"),
]