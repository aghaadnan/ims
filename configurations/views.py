from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import (DepartmentForm, 
                    ProvinceForm,CustomerGroupForm, InsuranceForm, BankForm, 
                    VehicleMakeForm, VehicleModelForm, PackageForm, ComplainTypesForm
                    
                    )
from .models import (
    Cities, Subscriptions,Province,
    Department, CustomerGroup, Insurance, Bank,
    VehicleMake, VehicleModel, Package, ComplainTypes, 
)

class CityListView(ListView):
    model = Cities
    template_name = 'configurations/city_list.html'


class CityCreateView(CreateView):
    model = Cities
    fields = ['city']
    template_name = 'configurations/city_form.html'
    success_url = reverse_lazy('configurations:city_list')


class CityUpdateView(UpdateView):
    model = Cities
    fields = ['city']
    template_name = 'configurations/city_form.html'
    success_url = reverse_lazy('configurations:city_list')


class CityDeleteView(DeleteView):
    model = Cities
    template_name = 'configurations/city_confirm_delete.html'
    success_url = reverse_lazy('configurations:city_list')


class SubscriptionListView(ListView):
    model = Subscriptions
    template_name = 'configurations/subscription_list.html'
    context_object_name = 'subscriptions'

class SubscriptionCreateView(CreateView):
    model = Subscriptions
    fields = ['subscription', 'days', 'price']

    template_name = 'configurations/subscription_form.html'
    success_url = reverse_lazy('configurations:subscription_list')


class SubscriptionUpdateView(UpdateView):
    model = Subscriptions
    fields = ['subscription']
    template_name = 'configurations/subscription_form.html'
    success_url = reverse_lazy('configurations:subscription_list')


class SubscriptionDeleteView(DeleteView):
    model = Subscriptions
    template_name = 'configurations/subscription_confirm_delete.html'
    success_url = reverse_lazy('configurations:subscription_list')


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'configurations/department/department_list.html'

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'configurations/department/department_create.html'
    success_url = reverse_lazy('configurations:department_list')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'configurations/department/department_create.html'
    success_url = reverse_lazy('configurations:department_list')

class DepartmentDetailView(DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'configurations/department/department_detail.html'

class DepartmentDeleteView(DeleteView):
    model = Department
    context_object_name = 'department'
    template_name = 'configurations/department/department_confirm_delete.html'
    success_url = reverse_lazy('configurations:department_list')


class ProvinceListView(ListView):
    model = Province
    template_name = 'configurations/province/province_list.html'
    context_object_name = 'provinces'

class ProvinceCreateView(CreateView):
    model = Province
    template_name = 'configurations/province/province_create.html'
    form_class = ProvinceForm
    success_url = reverse_lazy('configurations:province-list')

class ProvinceUpdateView(UpdateView):
    model = Province
    template_name = 'configurations/province/province_update.html'
    form_class = ProvinceForm
    success_url = reverse_lazy('configurations:province-list')

class ProvinceDetailView(DetailView):
    model = Province
    template_name = 'configurations/province/province_detail.html'
    context_object_name = 'province'

class ProvinceDeleteView(DeleteView):
    model = Province
    template_name = 'configurations/province/province_confirm_delete.html'
    success_url = reverse_lazy('configurations:province-list')

class CustomerGroupListView(ListView):
    model = CustomerGroup
    template_name = 'configurations/customergroup/customer_group_list.html'
    context_object_name = 'customer_group_list'

class CustomerGroupCreateView(CreateView):
    model = CustomerGroup
    template_name = 'configurations/customergroup/customer_group_create.html'
    form_class = CustomerGroupForm
    success_url = reverse_lazy('configurations:customer-group-list')

class CustomerGroupUpdateView(UpdateView):
    model = CustomerGroup
    template_name = 'configurations/customergroup/customer_group_update.html'
    form_class = CustomerGroupForm
    success_url = reverse_lazy('configurations:customer-group-list')

class CustomerGroupDeleteView(DeleteView):
    model = CustomerGroup
    template_name = 'configurations/customergroup/customer_group_confirm_delete.html'
    success_url = reverse_lazy('configurations:customer-group-list')

class InsuranceListView(ListView):
    model = Insurance
    template_name = 'configurations/insurance/insurance_list.html'

class InsuranceCreateView(CreateView):
    model = Insurance
    template_name = 'configurations/insurance/insurance_create.html'
    form_class = InsuranceForm

class InsuranceUpdateView(UpdateView):
    model = Insurance
    template_name = 'configurations/insurance/insurance_update.html'
    form_class = InsuranceForm

class InsuranceDeleteView(DeleteView):
    model = Insurance
    template_name = 'configurations/insurance/insurance_confirm_delete.html'
    success_url = '/configurations/insurance/'

class BankListView(ListView):
    model = Bank
    template_name = 'configurations/bank/bank_list.html'
    context_object_name = 'banks'


class BankCreateView(CreateView):
    model = Bank
    form_class = BankForm
    template_name = 'configurations/bank/bank_create.html'
    success_url = reverse_lazy('configurations:bank-list')


class BankUpdateView(UpdateView):
    model = Bank
    form_class = BankForm
    template_name = 'configurations/bank/bank_update.html'
    success_url = reverse_lazy('configurations:bank-list')


class BankDeleteView(DeleteView):
    model = Bank
    template_name = 'configurations/bank/bank_confirm_delete.html'
    success_url = reverse_lazy('configurations:bank-list')

class VehicleMakeListView(ListView):
    model = VehicleMake
    template_name = 'configurations/vehiclemake/vehicle_make_list.html'

class VehicleMakeCreateView(CreateView):
    model = VehicleMake
    form_class = VehicleMakeForm
    template_name = 'configurations/vehiclemake/vehicle_make_create.html'
    success_url = reverse_lazy('configurations:vehicle-make-list')

class VehicleMakeUpdateView(UpdateView):
    model = VehicleMake
    form_class = VehicleMakeForm
    template_name = 'configurations/vehiclemake/vehicle_make_update.html'
    success_url = reverse_lazy('configurations:vehicle-make-list')

class VehicleMakeDeleteView(DeleteView):
    model = VehicleMake
    template_name = 'configurations/vehiclemake/vehicle_make_confirm_delete.html'
    success_url = reverse_lazy('configurations:vehicle-make-list')

class VehicleModelListView(ListView):
    model = VehicleModel
    template_name = 'configurations/vehiclemodel/vehicle_model_list.html'

class VehicleModelCreateView(CreateView):
    model = VehicleModel
    form_class = VehicleModelForm
    template_name = 'configurations/vehiclemodel/vehicle_model_create.html'
    success_url = reverse_lazy('configurations:vehicle-model-list')

class VehicleModelUpdateView(UpdateView):
    model = VehicleModel
    form_class = VehicleModelForm
    template_name = 'configurations/vehiclemodel/vehicle_model_update.html'
    success_url = reverse_lazy('configurations:vehicle-model-list')

class VehicleModelDeleteView(DeleteView):
    model = VehicleModel
    template_name = 'configurations/vehiclemodel/vehicle_model_confirm_delete.html'
    success_url = reverse_lazy('configurations:vehicle-model-list')

class PackageListView(ListView):
    model = Package
    template_name = 'configurations/package/package_list.html'


class PackageCreateView(CreateView):
    model = Package
    form_class = PackageForm
    template_name = 'configurations/package/package_create.html'
    success_url = reverse_lazy('configurations:package-list')


class PackageUpdateView(UpdateView):
    model = Package
    form_class = PackageForm
    template_name = 'configurations/package/package_update.html'
    success_url = reverse_lazy('configurations:package-list')


class PackageDeleteView(DeleteView):
    model = Package
    template_name = 'configurations/package/package_confirm_delete.html'
    success_url = reverse_lazy('configurations:package-list')

class ComplainTypesListView(ListView):
    model = ComplainTypes
    template_name = 'configurations/complain_types_list.html'

class ComplainTypesCreateView(CreateView):
    model = ComplainTypes
    form_class = ComplainTypesForm
    template_name = 'configurations/complain_types_create.html'
    success_url = reverse_lazy('configurations:complain-types-list')

class ComplainTypesUpdateView(UpdateView):
    model = ComplainTypes
    form_class = ComplainTypesForm
    template_name = 'configurations/complain_types_update.html'
    success_url = reverse_lazy('configurations:complain-types-list')

class ComplainTypesDeleteView(DeleteView):
    model = ComplainTypes
    template_name = 'configurations/complain_types_confirm_delete.html'
    success_url = reverse_lazy('configurations:complain-types-list')