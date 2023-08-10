from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView

from profession.forms import Form
from profession.models import Profession



class ProfessionListView(ListView):
    model = Profession
    template_name = 'profession/list.html'
    context_object_name = 'professions'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', "")
        if search:
            queryset = queryset.filter(
                Q(name__contains=search))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', "")
        return context
class ProfessionCreateView(CreateView):
    model = Profession
    form_class = Form
    success_url = '/professions/list/'
    template_name = 'profession/form.html'
class ProfessionUpdateView(UpdateView):
    model = Profession
    form_class = Form
    success_url = '/professions/list/'
    template_name = 'profession/form.html'
class ProfessionDetailsView(DetailView):
    model = Profession
    template_name = 'profession/detail.html'
    context_object_name = 'profession'
def profession_delete(request, pk):
    profession = get_object_or_404(Profession, pk=pk)
    profession.delete()
    return redirect('professions-list')
