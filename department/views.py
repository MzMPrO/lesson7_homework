from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView

from branch.models import Branch
from department.forms import Form
from department.models import Department


class IndexView(TemplateView):
    template_name = 'index.html'


class DepartmentListView(ListView):
    model = Department
    template_name = 'department/list.html'
    context_object_name = 'departments'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', "")
        branch_id = self.request.GET.get('branch_id', "")
        if search:
            queryset = queryset.filter(
                Q(name__contains=search))
        if branch_id:
            queryset = queryset.filter(branch_id=branch_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branchs'] = Branch.objects.all()

        context['search'] = self.request.GET.get('search', "")
        context["branch_id"] = self.request.GET.get('branch_id', "")
        branch_id = self.request.GET.get('branch_id', "")
        if branch_id:
            branch_id = int(branch_id)
        else:
            branch_id = 0
        context["branch_id"] = branch_id


        return context
class DepartmentCreateView(CreateView):
    model = Department
    form_class = Form
    success_url = '/departments/list/'
    template_name = 'department/form.html'
class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = Form
    success_url = '/departments/list/'
    template_name = 'department/form.html'
class DepartmentDetailsView(DetailView):
    model = Department
    template_name = 'department/detail.html'
    context_object_name = 'department'
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect('departments-list')
