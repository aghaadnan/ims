from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Inventory, TrackerDevice
from companies.models import Company
from .forms import InventoryForm, TrackerDeviceForm, SimForm
from .models import Sim
import csv
from io import TextIOWrapper
from django.contrib import messages


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = self.request._messages
        if messages:
            context['messages'] = messages
        return context


    def get_queryset(self):
        company = self.request.user.company
        return TrackerDevice.objects.filter(company=company)

class TrackerDeviceDetailView(LoginRequiredMixin, DetailView):
    model = TrackerDevice
    template_name = 'inventory/trackerdevice_detail.html'
    context_object_name = 'trackerdevice_item'


# class TrackerDeviceCreateView(LoginRequiredMixin, CreateView):
     
 
#     model = TrackerDevice
#     template_name = 'inventory/trackerdevice_edit.html'
#     form_class = TrackerDeviceForm

#     def form_valid(self, form):
#         company = self.request.user.company
#         print(company)
#         trackerdevice_item = form.save(commit=False)
        
#         trackerdevice_item.user = self.request.user
#         print(trackerdevice_item.user)
#         trackerdevice_item.company = company
#         trackerdevice_item.save()
#         return redirect('inventory:trackerdevice_detail', pk=trackerdevice_item.pk)




# class TrackerDeviceCreateView(CreateView):
#     model = TrackerDevice
#     form_class = TrackerDeviceForm
#     template_name = 'inventory/trackerdevice_edit.html'
#     success_url = reverse_lazy('inventory:trackerdevice_list')

#     def form_valid(self, form):
#         tracker_device_list = []
#         imei_file = TextIOWrapper(self.request.FILES['csv_file'].file, encoding='utf-8')
#         reader = csv.reader(imei_file)
#         imei_list = [row[0] for row in reader if row]

#         if len(imei_list) != form.cleaned_data['quantity']:
#             return render(self.request, self.template_name, {'form': form, 'error_message': 'The quantity does not match the number of IMEI codes in the uploaded CSV file'})

#         for imei in imei_list:
#             tracker_device = TrackerDevice(
#                 model_number=form.cleaned_data['model_number'],
#                 vendor=form.cleaned_data['vendor'],
#                 price=form.cleaned_data['price'],
#                 imei=imei,
#                 isUsed=False,
#                 user=self.request.user,
#                 company=self.request.user.company,
#             )
#             tracker_device_list.append(tracker_device)

#         TrackerDevice.objects.bulk_create(tracker_device_list)

#         return redirect(self.success_url)


class TrackerDeviceCreateView(LoginRequiredMixin, CreateView):
    model = TrackerDevice
    template_name = 'inventory/trackerdevice_edit.html'
    form_class = TrackerDeviceForm

    def form_valid(self, form):
        company = self.request.user.company
        quantity = form.cleaned_data['quantity']
        csv_file = form.cleaned_data['csv_file']
        csv_data = csv_file.read().decode('utf-8')
        imei_list = csv_data.strip().split('\r\n')
        
        print(imei_list)
        if len(imei_list) != quantity:
            messages.error(self.request, 'The number of IMEIs does not match the quantity entered.')
            return redirect('inventory:trackerdevice_list')
        if len(set(imei_list)) != quantity:
            messages.error(self.request, 'The uploaded CSV contains duplicate IMEIs.')
            return redirect('inventory:trackerdevice_list')
        existing_imeis = TrackerDevice.objects.filter(imei__in=imei_list).values_list('imei', flat=True)
        print(set(imei_list))
        print('####')
        print(set(existing_imeis))
        new_imeis = set(imei_list) - set(existing_imeis)
        print(new_imeis)
        new_quantity = len(new_imeis)
        if new_quantity == 0:
            messages.error(self.request, 'All IMEIs in the CSV file already exist in the database.')
            return redirect('inventory:trackerdevice_list')
        trackerdevices = []
        for imei in new_imeis:
            trackerdevice = TrackerDevice(
                model_number=form.cleaned_data['model_number'],
                vendor=form.cleaned_data['vendor'],
                price=form.cleaned_data['price'],
                imei=imei,
                user=self.request.user,
                company=company,
            )
            trackerdevices.append(trackerdevice)
        TrackerDevice.objects.bulk_create(trackerdevices)
        messages.success(self.request, f'Successfully added {new_quantity} new tracker devices.')
        if existing_imeis:
            messages.error(self.request, f'{len(existing_imeis)} IMEIs in the CSV file already exist in the database.')
        return redirect('inventory:trackerdevice_list')








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
    #form_class = SimForm
    #success_url = reverse_lazy('inventory:sim_list')

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