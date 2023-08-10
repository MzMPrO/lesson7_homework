from django.urls import path

from department import views
from department.views import DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDetailsView, \
    department_delete, IndexView

urlpatterns = [
    path("", views.login_required(IndexView.as_view()), name="index"),
    path("departments/list/", views.login_required(DepartmentListView.as_view()), name="departments-list"),
    path("departments/create/", views.login_required(DepartmentCreateView.as_view()), name="departments-create"),
    path("departments/<int:pk>/update/", views.login_required(DepartmentUpdateView.as_view()), name="departments-Update"),
    path("departments/<int:pk>/detail/", views.login_required(DepartmentDetailsView.as_view()), name="departments-detail"),
    path("departments/<int:pk>/delete/", views.department_delete, name="departments-delete"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]