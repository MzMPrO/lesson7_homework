from django.urls import path

from branch import views

urlpatterns = [

    path("branchs/list/", views.BranchListView.as_view(), name="branchs-list"),
    path("branchs/create/", views.BranchCreateView.as_view(), name="branchs-create"),
    path("branchs/<int:pk>/update/", views.BranchUpdateView.as_view(), name="branchs-Update"),
    path("branchs/<int:pk>/detail/", views.BranchDetailsView.as_view(), name="branchs-detail"),
    path("branchs/<int:pk>/delete/", views.branch_delete, name="branchs-delete"),
]