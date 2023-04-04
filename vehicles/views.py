from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vehicle
from companies.models import Company


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'
    context_object_name = 'vehicle_list'
    paginate_by = 10

    def get_queryset(self):
        company = self.request.user.company
        return Vehicle.objects.filter(company=company)


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicles/vehicle_form.html'
    fields = ('RegistrationNumber', 'Make', 'Model', 'EngineNumber', 'ChesisNumber', 'Color', 'customer', 
              'trackerDevice', 'sim', 'isTrackerInstalled' )
             
    success_url = reverse_lazy('vehicles:vehicle_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = self.request.user.company
        return super().form_valid(form)





class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle_detail.html'
    context_object_name = 'vehicle'

class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = 'vehicles/vehicle_form.html'
    fields = ('RegistrationNumber', 'Make', 'Model', 'EngineNumber', 'ChesisNumber', 'Color')
    success_url = reverse_lazy('vehicles:vehicle_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicles:vehicle_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
