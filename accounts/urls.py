from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test
from . import views

app_name = 'accounts'

# # decorator to check if user is superuser
# def superuser_required(function=None):
#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and u.is_superuser,
#         login_url='/accounts/login/',
#         redirect_field_name=None
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator

urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', views.login_view, name='login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('staff/', views.StaffListView.as_view(), name='staff-list'),
    path('staff/create/', views.StaffCreateView.as_view(), name='staff-create'),
    path('staff/<int:pk>/update/', views.StaffUpdateView.as_view(), name='staff-update'),
    path('staff/<int:pk>/delete/', views.StaffDeleteView.as_view(), name='staff-delete'),
    path('usertype/', views.UserTypeListView.as_view(), name='usertype_list'),
    path('usertype/new/', views.UserTypeCreateView.as_view(), name='usertype_create'),
    path('usertype/<int:pk>/edit/', views.UserTypeUpdateView.as_view(), name='usertype_update'),
    path('usertype/<int:pk>/delete/', views.UserTypeDeleteView.as_view(), name='usertype_delete'),
    # path('userprofiles/create/', superuser_required(views.UserProfileCreateView.as_view()), name='userprofile_create'),
    # path('userprofiles/', superuser_required(views.UserProfileListView.as_view()), name='userprofile_list'),
    # path('userprofiles/<int:pk>/update/', superuser_required(views.UserProfileUpdateView.as_view()), name='userprofile_edit'),
    # path('userprofiles/<int:pk>/delete/', superuser_required(views.UserProfileDeleteView.as_view()), name='userprofile_delete'),
    path('userprofiles/create/', views.UserProfileCreateView.as_view(), name='userprofile_create'),
    path('userprofiles/', views.UserProfileListView.as_view(), name='userprofile_list'),
    path('userprofiles/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name='userprofile_edit'),
    path('userprofiles/<int:pk>/delete/', views.UserProfileDeleteView.as_view(), name='userprofile_delete'),
]
