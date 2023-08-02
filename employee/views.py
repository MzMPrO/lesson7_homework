from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView

from department.models import Department
from employee.forms import Form
from employee.models import Employee
from profession.models import Profession


class IndexView(TemplateView):
    template_name = 'index.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', "")
        department_id = self.request.GET.get('department_id', "")
        profession_id = self.request.GET.get('profession_id', "")
        if search:
            queryset = queryset.filter(
                Q(first_name__contains=search) | Q(last_name__contains=search))
        if department_id:
            queryset = queryset.filter(department_id=department_id)
        if profession_id:
            queryset = queryset.filter(profession_id=profession_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['professions'] = Profession.objects.all()

        context['search'] = self.request.GET.get('search', "")
        context["department_id"] = self.request.GET.get('department_id', "")
        context["profession_id"] = self.request.GET.get('profession_id', "")
        department_id = self.request.GET.get('department_id', "")
        if department_id:
            department_id = int(department_id)
        else:
            department_id = 0
        context["department_id"] = department_id

        profession_id = self.request.GET.get('profession_id', "")
        if profession_id:
            profession_id = int(profession_id)
        else:
            profession_id = 0
        context["profession_id"] = profession_id

        return context
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = Form
    success_url = '/employees/list/'
    template_name = 'employee/form.html'
class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = Form
    success_url = '/employees/list/'
    template_name = 'employee/form.html'
class EmployeeDetailsView(DetailView):
    model = Employee
    template_name = 'employee/detail.html'
    context_object_name = 'employee'
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employees-list')
