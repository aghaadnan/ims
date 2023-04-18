from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import UserProfile, UserType
from django.urls import reverse, reverse_lazy
from django import forms
from django.http import Http404

class LandingPageView(TemplateView):
    template_name = "landing_page.html"



class CustomLoginView(LoginView):

    def form_invalid(self, form):
        messages.error(self.request, 'Incorrect username or password.')
        
        return super().form_invalid(form)

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active and not user.is_superuser:
            messages.error(self.request, 'User is inactive. Contact administrator.')
            return self.form_invalid(form)
        return super().form_valid(form)






def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.instance.is_admin = True
            user = form.save()
            login(request, user)
            return redirect('landing-page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required

def login_view(request):
  return True
    
# def login_view(request):
#     if request.user.is_authenticated:
#         if request.user.is_manager or request.user.is_admin:
#             return redirect('inventory:item_list')
#         elif request.user.is_superuser:
#             return redirect('home:company_list')
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 if user.is_manager or request.user.is_admin:
#                     return redirect('inventory:inventory_list')
#                 elif user.is_superuser:
#                     return redirect('home:company_list')
                
            
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})


@login_required
def redirect_user(request):
    if request.user.is_superuser:
        print("Redirecting to /dashboards/")
        return redirect('/dashboards/')
    elif request.user.is_admin:
        print("Redirecting to /inventory/")
        return redirect('/inventory/')
    else:
        print("Redirecting to /accounts/profile/")
        return redirect('/accounts/profile/')
def profile_view(request):
    user_profile = request.user
    context = {'user_profile': user_profile}
    return render(request, 'registration/profile.html', context)

@method_decorator(login_required, name='dispatch')
class StaffListView(UserPassesTestMixin, ListView):
    model = UserProfile
    template_name = 'registration/staff_list.html'
    context_object_name = 'staff_list'

    def test_func(self):
        # Check if the user is a manager for their company
        return self.request.user.is_admin

    def get_queryset(self):
        # Only show staff accounts for the current user's company
        return self.model.objects.filter(company=self.request.user.company)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title_left'] = 'Staff list'
        return context

# @method_decorator(login_required, name='dispatch')
# class StaffCreateView(UserPassesTestMixin, CreateView):
#     model = UserProfile
#     template_name = 'registration/staff_form.html'
#     fields = ['username', 'first_name', 'last_name', 'email', 'password', 'usertype', 'is_active', ]

#     def test_func(self):
#         # Check if the user is a manager for their company
#         return self.request.user.is_manager

#     def form_valid(self, form):
#         # Set the user's company to the current user's company
#         form.instance.company = self.request.user.company
#         # Set the user's password
#         form.instance.set_password(form.cleaned_data['password'])
#         form.instance.is_manager = False
#         form.instance.is_staff = False
#         # Save the form
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         return reverse('accounts:staff-list')

from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class StaffCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Your password must contain at least 8 characters.",
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    # OPERATOR_CHOICES = (
    #     ('Manager', 'Manager'),
    #     ('Agent', 'Agent'),
    #     ('Installer', 'Installer'),
    
    # )
    # usertype = forms.ChoiceField(choices=OPERATOR_CHOICES)
    class Meta:
        
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email','usertype', 'is_active']
        def clean_usertype(self):
            usertype = self.cleaned_data.get('usertype')
            if not usertype:
                raise forms.ValidationError("You must select a user type.")
            return usertype
class StaffCreateView(UserPassesTestMixin, CreateView):
    model = UserProfile
    template_name = 'registration/staff_form.html'
    form_class = StaffCreationForm

    def test_func(self):
        # Check if the user is a manager for their company
        return self.request.user.is_admin

    def form_valid(self, form):
        # Set the user's company to the current user's company
        form.instance.company = self.request.user.company
        # Set the user's password
        form.instance.set_password(form.cleaned_data['password1'])
        # Set the user's user type
        # usertype = form.cleaned_data['usertype']
        # if usertype == 'Manager':
        #     form.instance.is_manager = True
        # elif usertype == 'Agent':
        #     form.instance.is_agent = True
        # elif usertype == 'Installer':
        #     form.instance.is_installer = True
        form.instance.is_admin = False
        # form.instance.is_staff = False
        # Save the form
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accounts:staff-list')


class StaffUpdateForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        ('manager', 'Manager'),
        ('agent', 'Agent'),
        ('installer', 'Installer')
    )

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']

    def save(self, commit=True):
        instance = super().save(commit=False)
        user_type = self.cleaned_data['user_type']
        if user_type == 'manager':
            instance.is_manager = True
            instance.is_agent = False
            instance.is_installer = False
        elif user_type == 'agent':
            instance.is_manager = False
            instance.is_agent = True
            instance.is_installer = False
        elif user_type == 'installer':
            instance.is_manager = False
            instance.is_agent = False
            instance.is_installer = True
        if commit:
            instance.save()
        return instance

class StaffUpdateView(UserPassesTestMixin, UpdateView):
    model = UserProfile
    template_name = 'registration/staff_form.html'
    form_class = StaffUpdateForm

    def test_func(self):
        # Check if the user is a manager for their company
        return self.request.user.is_admin

    def get_success_url(self):
        return reverse('accounts:staff-list')

# @method_decorator(login_required, name='dispatch')
# class StaffUpdateView(UserPassesTestMixin, UpdateView):
#     model = UserProfile
#     template_name = 'registration/staff_form.html'
#     fields = ['username', 'first_name', 'last_name', 'email', 'is_active']

#     def test_func(self):
#         # Check if the user is a manager for their company
#         return self.request.user.is_admin
#     def get_success_url(self):
#         return reverse('accounts:staff-list')

@method_decorator(login_required, name='dispatch')
class StaffDeleteView(UserPassesTestMixin, DeleteView):
    model = UserProfile
    template_name = 'registration/staff_confirm_delete.html'

    def test_func(self):
        # Check if the user is a manager for their company
        return self.request.user.is_admin

    def get_success_url(self):
        messages.success(self.request, "Staff account deleted successfully.")
        return reverse('accounts:staff-list')



@method_decorator(login_required, name='dispatch')
class UserTypeListView(ListView):
    model = UserType
    template_name = 'accounts/usertype_list.html'
    context_object_name = 'usertypes'
@method_decorator(login_required, name='dispatch')
class UserTypeCreateView(CreateView):
    model = UserType
    template_name = 'accounts/usertype_form.html'
    fields = ['usertype']
    success_url = reverse_lazy('accounts:usertype_list')

class UserTypeUpdateView(UpdateView):
    model = UserType
    template_name = 'accounts/usertype_form.html'
    fields = ['usertype']
    success_url = reverse_lazy('accounts:usertype_list')

class UserTypeDeleteView(DeleteView):
    model = UserType
    template_name = 'accounts/usertype_confirm_delete.html'
    success_url = reverse_lazy('accounts:usertype_list')


class SuperAdminRequiredMixin(UserPassesTestMixin):
    """
    Mixin to restrict view access to super admin users only.
    """
    def test_func(self):
        return self.request.user.is_superuser

class UserProfileListView(SuperAdminRequiredMixin, ListView):
    """
    View to display a list of user profiles.
    """
    model = UserProfile
    template_name = 'accounts/userprofile_list.html'
    context_object_name = 'userprofiles'

class UserProfileCreateView(SuperAdminRequiredMixin, CreateView):
    """
    View to create a new user profile.
    """
    model = UserProfile
    template_name = 'accounts/userprofile_form.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'is_admin', 'is_agent', 'company', 'usertype']
    success_url = reverse_lazy('userprofile_list')

class UserProfileUpdateView(SuperAdminRequiredMixin, UpdateView):
    """
    View to update an existing user profile.
    """
    model = UserProfile
    template_name = 'accounts/userprofile_form.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'is_admin', 'is_agent', 'company', 'usertype']
    success_url = reverse_lazy('userprofile_list')



class UserProfileDeleteView(SuperAdminRequiredMixin, DeleteView):
    """
    View to delete an existing user profile.
    """
    model = UserProfile
    template_name = 'accounts/userprofile_confirm_delete.html'
    success_url = reverse_lazy('accounts:userprofile_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Prevent deletion of super admins
        if self.object.is_superuser:
            raise Http404("Cannot delete super admin")

        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

