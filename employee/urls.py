from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("employees/list/", views.EmployeeListView.as_view(), name="employees-list"),
    path("employees/create/", views.EmployeeCreateView.as_view(), name="employees-create"),
    path("employees/<int:pk>/update/", views.EmployeeUpdateView.as_view(), name="employees-Update"),
    path("employees/<int:pk>/detail/", views.EmployeeDetailsView.as_view(), name="employees-detail"),
    path("employees/<int:pk>/delete/", views.employee_delete, name="employees-delete"),
]