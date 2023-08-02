from django.urls import path

from . import views

urlpatterns = [
    path("professions/list/", views.ProfessionListView.as_view(), name="professions-list"),
    path("professions/create/", views.ProfessionCreateView.as_view(), name="professions-create"),
    path("professions/<int:pk>/update/", views.ProfessionUpdateView.as_view(), name="professions-Update"),
    path("professions/<int:pk>/detail/", views.ProfessionDetailsView.as_view(), name="professions-detail"),
    path("professions/<int:pk>/delete/", views.profession_delete, name="professions-delete"),
]