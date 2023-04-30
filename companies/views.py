from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm, EmailTemplateForm, SmsTemplateForm
from .models import Company, EmailTemplate, SmsTemplate
from accounts.models import UserProfile
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
@login_required
def company_list(request):
    companies = Company.objects.filter(owner=request.user)
    return render(request, 'companies/company_list.html', {'companies': companies})

# @login_required
# def company_detail(request, pk):
#     company = get_object_or_404(Company, pk=pk, owner=request.user)
#     return render(request, 'companies/company_detail.html', {'company': company})
@login_required
def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk, owner=request.user)
    users = UserProfile.objects.filter(company=company)
    return render(request, 'companies/company_detail.html', {'company': company, 'users': users})


@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            return redirect('home:company_detail', pk=company.pk)
    else:
        form = CompanyForm()
    return render(request, 'companies/company_form.html', {'form': form})

@login_required
def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save()
            return redirect('company_detail', pk=company.pk)
    else:
        form = CompanyForm(instance=company)
    return render(request, 'companies/company_form.html', {'form': form})
    
@login_required
def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk, owner=request.user)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'companies/company_confirm_delete.html', {'company': company})




@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'companies/company_list.html'
@method_decorator(login_required, name='dispatch')
class CompanyDetailView(DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'companies/company_detail.html'


@method_decorator(login_required, name='dispatch')
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('companies:company_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_edit.html'
    success_url = reverse_lazy('companies:company_list')
    
@method_decorator(login_required, name='dispatch')
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'companies/company_confirm_delete.html'
    success_url = reverse_lazy('company-list')

@csrf_exempt
def toggle_company_status(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        is_active = request.POST.get('is_active')
        if is_active.lower() == 'true':
            is_active = True
        elif is_active.lower() == 'false':
            is_active = False
        company = Company.objects.get(id=company_id)
        users = UserProfile.objects.filter(company=company)
        print(users)
        if users.exists():
            for user in users:
                user.is_active = is_active
                user.save()
        company.is_active = is_active
        company.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

class CompanyStatusUpdateView(View):

    def post(self, request, *args, **kwargs):
        company_id = kwargs['pk']
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            return redirect('home:company_list')
        is_active = bool(request.POST.get('is_active'))
        company.is_active = is_active
        company.save()
        return redirect('home:company_list')



class EmailTemplateListView(ListView):
    model = EmailTemplate
    template_name = 'email_templates/email_template_list.html'
    context_object_name = 'email_templates'

class EmailTemplateDetailView(DetailView):
    model = EmailTemplate
    template_name = 'email_templates/email_template_detail.html'
    context_object_name = 'email_template'


class EmailTemplateCreateView(CreateView):
    model = EmailTemplate
    form_class = EmailTemplateForm
    template_name = 'email_templates/email_template_create.html'
    success_url = reverse_lazy('companies:email_template_list')

class EmailTemplateUpdateView(UpdateView):
    model = EmailTemplate
    form_class = EmailTemplateForm
    context_object_name = 'email_templates'
    template_name = 'email_templates/email_template_update.html'
    success_url = reverse_lazy('companies:email_template_list')

class EmailTemplateDeleteView(DeleteView):
    model = EmailTemplate
    template_name = 'email_templates/email_template_confirm_delete.html'
    success_url = reverse_lazy('email_templates:list')

class SmsTemplateListView(ListView):
    model = SmsTemplate
    template_name = 'sms_templates/sms_template_list.html'
    context_object_name = 'sms_templates'

class SmsTemplateCreateView(CreateView):
    model = SmsTemplate
    form_class = SmsTemplateForm
    template_name = 'sms_templates/sms_template_create.html'
    success_url = reverse_lazy('companies:sms_template_list')

class SmsTemplateUpdateView(UpdateView):
    model = SmsTemplate
    form_class = SmsTemplateForm
    template_name = 'sms_templates/sms_template_update.html'
    success_url = reverse_lazy('companies:sms_template_list')

class SmsTemplateDeleteView(DeleteView):
    model = SmsTemplate
    success_url = reverse_lazy('companies:sms_template_list')

class SmsTemplateDetailView(DetailView):
    model = SmsTemplate
    context_object_name = 'sms_template'