from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm
from .models import Company
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
    success_url = reverse_lazy('companies:company_detail')
    
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
