from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Inventory, TrackerDevice
from companies.models import Company
from .forms import InventoryForm, TrackerDeviceForm
from .models import Sim


class InventoryListView(LoginRequiredMixin, ListView):
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'

    def get_queryset(self):
        company = self.request.user.company
        return Inventory.objects.filter(company=company)


class InventoryDetailView(LoginRequiredMixin, DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'inventory_item'


class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    template_name = 'inventory/inventory_edit.html'
    form_class = InventoryForm

    def form_valid(self, form):
        company = self.request.user.company
        print(company)
        inventory_item = form.save(commit=False)
        
        inventory_item.user = self.request.user
        print(inventory_item.user)
        inventory_item.company = company
        inventory_item.save()
        return redirect('inventory_detail', pk=inventory_item.pk)


class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Inventory
    template_name = 'inventory/inventory_edit.html'
    form_class = InventoryForm

    def get_object(self, queryset=None):
        company = self.request.user.company
        obj = super().get_object(queryset=queryset)
        if obj.company != company:
            raise Http404()
        return obj

    def form_valid(self, form):
        company = self.request.user.company
        inventory_item = form.save(commit=False)
        inventory_item.user = self.request.user
        inventory_item.company = company
        inventory_item.save()
        return redirect('inventory_detail', pk=inventory_item.pk)


class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')

    def get_object(self, queryset=None):
        company = self.request.user.company
        obj = super().get_object(queryset=queryset)
        if obj.company != company:
            raise Http404()
        return obj


class TrackerDeviceListView(LoginRequiredMixin, ListView):
    template_name = 'inventory/trackerdevice_list.html'
    context_object_name = 'trackerdevice_items'

    def get_queryset(self):
        company = self.request.user.company
        return TrackerDevice.objects.filter(company=company)

class TrackerDeviceDetailView(LoginRequiredMixin, DetailView):
    model = TrackerDevice
    template_name = 'inventory/trackerdevice_detail.html'
    context_object_name = 'trackerdevice_item'


class TrackerDeviceCreateView(LoginRequiredMixin, CreateView):
    model = TrackerDevice
    template_name = 'inventory/trackerdevice_edit.html'
    form_class = TrackerDeviceForm

    def form_valid(self, form):
        company = self.request.user.company
        print(company)
        trackerdevice_item = form.save(commit=False)
        
        trackerdevice_item.user = self.request.user
        print(trackerdevice_item.user)
        trackerdevice_item.company = company
        trackerdevice_item.save()
        return redirect('inventory:trackerdevice_detail', pk=trackerdevice_item.pk)
    
class TrackerDeviceUpdateView(LoginRequiredMixin, UpdateView):
    model = TrackerDevice
    template_name = 'inventory/trackerdevice_edit.html'
    form_class = TrackerDeviceForm

    def get_object(self, queryset=None):
        company = self.request.user.company
        obj = super().get_object(queryset=queryset)
        if obj.company != company:
            raise Http404()
        return obj

    def form_valid(self, form):
        company = self.request.user.company
        trackerdevice_item = form.save(commit=False)
        trackerdevice_item.user = self.request.user
        trackerdevice_item.company = company
        trackerdevice_item.save()
        return redirect('inventory:trackerdevice_detail', pk=trackerdevice_item.pk)
    

class TrackerDeviceDeleteView(LoginRequiredMixin, DeleteView):
    model = TrackerDevice
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:trackerdevice_list')

    def get_object(self, queryset=None):
        company = self.request.user.company
        obj = super().get_object(queryset=queryset)
        if obj.company != company:
            raise Http404()
        return obj


class SimListView(LoginRequiredMixin, ListView):
    model = Sim
    template_name = 'inventory/sim_list.html'
    context_object_name = 'sim_items'
    def get_queryset(self):
        company = self.request.user.company
        return Sim.objects.filter(company=company)
class SimCreateView(LoginRequiredMixin, CreateView):
    model = Sim
    template_name = 'inventory/sim_form.html'
    fields = ['MSISDN', 'ICC_ID', 'OPERATOR', 'SIM_TYPE', 'PACKAGE']
    success_url = reverse_lazy('inventory:sim_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = self.request.user.company
        return super().form_valid(form)



class SimUpdateView(UpdateView):
    model = Sim
    template_name = 'inventory/sim_form.html'
    fields = ['MSISDN', 'ICC_ID', 'OPERATOR', 'SIM_TYPE', 'PACKAGE']
    success_url = reverse_lazy('inventory:sim_list')


class SimDeleteView(DeleteView):
    model = Sim
    success_url = reverse_lazy('inventory:sim_list')
    template_name = 'inventory/sim_confirm_delete.html'