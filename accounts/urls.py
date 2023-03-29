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
    
]
