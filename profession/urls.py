from django.urls import path

from profession import views
from profession.views import ProfessionListView, ProfessionCreateView, ProfessionUpdateView, ProfessionDetailsView
from department.views import login_required

urlpatterns = [
    path("professions/list/", login_required(ProfessionListView.as_view()), name="professions-list"),
    path("professions/create/", login_required(ProfessionCreateView.as_view()), name="professions-create"),
    path("professions/<int:pk>/update/", login_required(ProfessionUpdateView.as_view()), name="professions-Update"),
    path("professions/<int:pk>/detail/", login_required(ProfessionDetailsView.as_view()), name="professions-detail"),
    path("professions/<int:pk>/delete/", views.profession_delete, name="professions-delete"),
]