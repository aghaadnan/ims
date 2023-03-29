from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm
from .models import Company
from accounts.models import UserProfile

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
