from django.shortcuts import render
from django.views.generic import TemplateView
from companies.models import Company
from leads.models import SalesLead
from accounts.models import UserProfile
from django.utils import timezone
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SuperAdminRequiredMixin(UserPassesTestMixin):
    """
    Mixin to restrict view access to super admin users only.
    """
    def test_func(self):
        return self.request.user.is_superuser

class DashboardView(SuperAdminRequiredMixin,TemplateView):
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






class AdminDashboardView(TemplateView):
    template_name = 'dashboards/companydash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = timezone.now().date()
        week_start = today - datetime.timedelta(days=today.weekday())
        month_start = today.replace(day=1)
        year_start = today.replace(month=1, day=1)

        context['today_leads'] = SalesLead.objects.filter(datetime__exact=today).count()
        context['week_leads'] = SalesLead.objects.filter(datetime__range=(week_start, today)).count()
        context['month_leads'] = SalesLead.objects.filter(datetime__range=(month_start, today)).count()
        context['year_leads'] = SalesLead.objects.filter(datetime__range=(year_start, today)).count()
        context['new_leads'] = SalesLead.objects.filter(status__exact='new').count()
        context['confirmed_leads'] = SalesLead.objects.filter(status__exact='confirmed').count()
        context['rejected_leads'] = SalesLead.objects.filter(status__exact='rejected').count()
        context['installed_leads'] = SalesLead.objects.filter(status__exact='installed').count()
        return context


