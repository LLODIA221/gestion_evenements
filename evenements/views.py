from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect  
from .models import Evenement



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def get_queryset(self):
    return Evenement.objects.filter(cree_par=self.request.user).order_by('-date')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class EvenementListView(LoginRequiredMixin, ListView):
    model = Evenement
    template_name = 'evenements/list.html'
    context_object_name = 'evenements'

class EvenementDetailView(LoginRequiredMixin, DetailView):
    model = Evenement
    template_name = 'evenements/detail.html'

class EvenementCreateView(LoginRequiredMixin, CreateView):
    model = Evenement
    fields = ['titre', 'description', 'date', 'lieu']
    template_name = 'evenements/form.html'
    success_url = reverse_lazy('evenement_list')

    def form_valid(self, form):
        form.instance.cree_par = self.request.user
        return super().form_valid(form)

class EvenementUpdateView(LoginRequiredMixin, UpdateView):
    model = Evenement
    fields = ['titre', 'description', 'date', 'lieu']
    template_name = 'evenements/form.html'
    success_url = reverse_lazy('evenement_list')

class EvenementDeleteView(LoginRequiredMixin, DeleteView):
    model = Evenement
    template_name = 'evenements/confirm_delete.html'
    success_url = reverse_lazy('evenement_list')

