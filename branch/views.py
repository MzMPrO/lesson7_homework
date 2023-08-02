from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView

from branch.forms import Form
from branch.models import Branch


class IndexView(TemplateView):
    template_name = 'index.html'


class BranchListView(ListView):
    model = Branch
    template_name = 'branch/list.html'
    context_object_name = 'branchs'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', "")
        if search:
            queryset = queryset.filter(
                Q(name__contains=search) | Q(address__contains=search))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', "")
        return context
class BranchCreateView(CreateView):
    model = Branch
    form_class = Form
    success_url = '/branchs/list/'
    template_name = 'branch/form.html'
class BranchUpdateView(UpdateView):
    model = Branch
    form_class = Form
    success_url = '/branchs/list/'
    template_name = 'branch/form.html'
class BranchDetailsView(DetailView):
    model = Branch
    template_name = 'branch/detail.html'
    context_object_name = 'branch'
def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    branch.delete()
    return redirect('branchs-list')
