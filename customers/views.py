from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from companies.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        company = self.request.user.company
        return Customer.objects.filter(company=company)


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['Name', 'ContactNumber', 'Address']
    success_url = reverse_lazy('customers:customer_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['Name', 'ContactNumber', 'Address']
    success_url = reverse_lazy('customers:customer_list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customers:customer_list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
