from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from accounts.models import UserProfile
from .models import TrackerInstallation
from customers.models import Customer
from vehicles.models import Vehicle
from inventory.models import TrackerDevice, Sim
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from .models import TrackerInstallation

class TrackerInstallationListView(LoginRequiredMixin, ListView):
    model = TrackerInstallation
    context_object_name = 'installations'
    template_name = 'installations/tracker_installation_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # only show installations for the current user's company
        queryset = queryset.filter(company=self.request.user.company)
        return queryset

class TrackerInstallationCreateView(LoginRequiredMixin, CreateView):
    model = TrackerInstallation
    fields = ['vehicle', 'tracker_device', 'sim', 'installed_by']
    template_name = 'installations/tracker_installation_form.html'
    success_url = reverse_lazy('installations:tracker-installation-list')

    def form_valid(self, form):
        # Set the company to the current user's company
        form.instance.company = self.request.user.company
        # Set the user who installed the tracker to the current user
        #form.instance.installed_by = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # If the user is an installer, set the installed_by field to the current user and disable it
        if self.request.user.is_installer:
            form.fields['installed_by'].initial = self.request.user
            form.fields['installed_by'].widget.attrs['readonly'] = True
        # If the user is a manager, limit the installed_by field choices to installers in their company
        elif self.request.user.is_manager or self.request.user.is_admin:
            form.fields['installed_by'].queryset = UserProfile.objects.filter(company=self.request.user.company, is_installer=True)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add related objects to the context
        context['customers'] = Customer.objects.all()
        context['vehicles'] = Vehicle.objects.all()
        context['tracker_devices'] = TrackerDevice.objects.all()
        context['sims'] = Sim.objects.all()
        return context



class TrackerInstallationUpdateView(UpdateView):
    model = TrackerInstallation
    template_name = 'installations/tracker_installation_form.html'
    fields = ['vehicle', 'tracker_device', 'sim', 'installed_by']
    success_url = reverse_lazy('installations:tracker-installation-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # If the user is an installer, set the installed_by field to the current user and disable it
        if self.request.user.is_installer:
            form.fields['installed_by'].initial = self.request.user
            form.fields['installed_by'].widget.attrs['readonly'] = True
        # If the user is a manager, limit the installed_by field choices to installers in their company
        elif self.request.user.is_manager or self.request.user.is_admin:
            form.fields['installed_by'].queryset = UserProfile.objects.filter(company=self.request.user.company, is_installer=True)
        return form


class TrackerInstallationDeleteView(DeleteView):
    model = TrackerInstallation
    template_name = 'installations/trackerinstallation_confirm_delete.html'
    success_url = reverse_lazy('installations:tracker-installation-list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(company=self.request.user.company)