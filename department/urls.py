from django.urls import path

from department import views

urlpatterns = [
    path("departments/list/", views.DepartmentListView.as_view(), name="departments-list"),
    path("departments/create/", views.DepartmentCreateView.as_view(), name="departments-create"),
    path("departments/<int:pk>/update/", views.DepartmentUpdateView.as_view(), name="departments-Update"),
    path("departments/<int:pk>/detail/", views.DepartmentDetailsView.as_view(), name="departments-detail"),
    path("departments/<int:pk>/delete/", views.department_delete, name="departments-delete"),
]