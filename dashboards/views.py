from django.shortcuts import render
from django.views.generic import TemplateView
from companies.models import Company
from accounts.models import UserProfile

class DashboardView(TemplateView):
    template_name = 'dashboards/superdash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_companies = Company.objects.count()
        active_companies = Company.objects.filter(is_active=True).count()
        inactive_companies = Company.objects.filter(is_active=False).count()
        total_users = UserProfile.objects.count()
        active_users = UserProfile.objects.filter(is_active=True).count()
        inactive_users = UserProfile.objects.filter(is_active=False).count()
        context['total_companies'] = total_companies
        context['active_companies'] = active_companies
        context['inactive_companies'] = inactive_companies
        context['total_users'] = total_users
        context['active_users'] = active_users
        context['inactive_users'] = inactive_users
        return context

