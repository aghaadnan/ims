from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path("logout/", LogoutView.as_view(next_page='landing-page'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('staff/', views.StaffListView.as_view(), name='staff-list'),
    path('staff/create/', views.StaffCreateView.as_view(), name='staff-create'),
    path('staff/<int:pk>/update/', views.StaffUpdateView.as_view(), name='staff-update'),
    path('staff/<int:pk>/delete/', views.StaffDeleteView.as_view(), name='staff-delete'),
    path('usertype/', views.UserTypeListView.as_view(), name='usertype_list'),
    path('usertype/new/', views.UserTypeCreateView.as_view(), name='usertype_create'),
    path('usertype/<int:pk>/edit/', views.UserTypeUpdateView.as_view(), name='usertype_update'),
    path('usertype/<int:pk>/delete/', views.UserTypeDeleteView.as_view(), name='usertype_delete'),
]
