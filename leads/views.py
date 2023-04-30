from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import SalesLead
from .forms import SalesLeadForm

class SalesLeadListView(ListView):
    model = SalesLead
    template_name = "leads/sales_lead_list.html"
    context_object_name = "leads"
    def get_queryset(self):
        return SalesLead.objects.order_by('datetime')  # Order by date in descending order

class SalesLeadCreateView(CreateView):
    model = SalesLead
    form_class = SalesLeadForm
    template_name = "leads/sales_lead_create.html"
    success_url = reverse_lazy("leads:sales-lead-list")

    def form_valid(self, form):
        form.instance.status = 'new'
        return super().form_valid(form)

class SalesLeadUpdateView(UpdateView):
    model = SalesLead
    form_class = SalesLeadForm
    template_name = "leads/sales_lead_update.html"
    success_url = reverse_lazy("leads:sales-lead-list")

class SalesLeadDeleteView(DeleteView):
    model = SalesLead
    template_name = "leads/sales_lead_confirm_delete.html"
    success_url = reverse_lazy("leads:sales-lead-list")

