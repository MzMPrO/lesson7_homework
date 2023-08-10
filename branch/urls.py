from django.urls import path

from branch import views
from branch.views import BranchListView, BranchCreateView, BranchUpdateView, BranchDetailsView
from department.views import login_required

urlpatterns = [
    path("branchs/list/", login_required(BranchListView.as_view()), name="branchs-list"),
    path("branchs/create/", login_required(BranchCreateView.as_view()), name="branchs-create"),
    path("branchs/<int:pk>/update/", login_required(BranchUpdateView.as_view()), name="branchs-Update"),
    path("branchs/<int:pk>/detail/", login_required(BranchDetailsView.as_view()), name="branchs-detail"),
    path("branchs/<int:pk>/delete/", views.branch_delete, name="branchs-delete"),
]
