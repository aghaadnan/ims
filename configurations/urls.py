from django.urls import path
from . import views
from .views import (
    DepartmentListView,
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDetailView,
    DepartmentDeleteView,
)
app_name = 'configurations'

urlpatterns = [
    path('cities/', views.CityListView.as_view(), name='city_list'),
    path('cities/create/', views.CityCreateView.as_view(), name='city_create'),
    path('cities/<int:pk>/', views.CityUpdateView.as_view(), name='city_update'),
    path('cities/<int:pk>/delete/', views.CityDeleteView.as_view(), name='city_delete'),
    
    path('subscriptions/', views.SubscriptionListView.as_view(), name='subscription_list'),
    path('subscriptions/create/', views.SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscriptions/<int:pk>/', views.SubscriptionUpdateView.as_view(), name='subscription_update'),
    path('subscriptions/<int:pk>/delete/', views.SubscriptionDeleteView.as_view(), name='subscription_delete'),

    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/detail/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'),

    path('provinces/', views.ProvinceListView.as_view(), name='province-list'),
    path('provinces/create/', views.ProvinceCreateView.as_view(), name='province-create'),
    path('provinces/<int:pk>/update/', views.ProvinceUpdateView.as_view(), name='province-update'),
    path('provinces/<int:pk>/', views.ProvinceDetailView.as_view(), name='province-detail'),
    path('provinces/<int:pk>/delete/', views.ProvinceDeleteView.as_view(), name='province-delete'),

    path('customer-group/', views.CustomerGroupListView.as_view(), name='customer-group-list'),
    path('customer-group/create/', views.CustomerGroupCreateView.as_view(), name='customer-group-create'),
    path('customer-group/update/<int:pk>/', views.CustomerGroupUpdateView.as_view(), name='customer-group-update'),
    path('customer-group/delete/<int:pk>/', views.CustomerGroupDeleteView.as_view(), name='customer-group-delete'),

    path('insurance/', views.InsuranceListView.as_view(), name='insurance-list'),
    path('insurance/create/', views.InsuranceCreateView.as_view(), name='insurance-create'),
    path('insurance/update/<int:pk>/', views.InsuranceUpdateView.as_view(), name='insurance-update'),
    path('insurance/delete/<int:pk>/', views.InsuranceDeleteView.as_view(), name='insurance-delete'),

    path('banks/', views.BankListView.as_view(), name='bank-list'),
    path('banks/create/', views.BankCreateView.as_view(), name='bank-create'),
    path('banks/update/<int:pk>/', views.BankUpdateView.as_view(), name='bank-update'),
    path('banks/delete/<int:pk>/', views.BankDeleteView.as_view(), name='bank-delete'),

    path('vehicle-makes/', views.VehicleMakeListView.as_view(), name='vehicle-make-list'),
    path('vehicle-makes/create/', views.VehicleMakeCreateView.as_view(), name='vehicle-make-create'),
    path('vehicle-makes/<int:pk>/update/', views.VehicleMakeUpdateView.as_view(), name='vehicle-make-update'),
    path('vehicle-makes/<int:pk>/delete/', views.VehicleMakeDeleteView.as_view(), name='vehicle-make-delete'),

    path('vehicle-model/', views.VehicleModelListView.as_view(), name='vehicle-model-list'),
    path('vehicle-model/create/',views.VehicleModelCreateView.as_view(), name='vehicle-model-create'),
    path('vehicle-model/<int:pk>/update/', views.VehicleModelUpdateView.as_view(), name='vehicle-model-update'),
    path('vehicle-model/<int:pk>/delete/',views.VehicleModelDeleteView.as_view(), name='vehicle-model-delete'),

    path('packages/', views.PackageListView.as_view(), name='package-list'),
    path('packages/create/', views.PackageCreateView.as_view(), name='package-create'),
    path('packages/update/<int:pk>/', views.PackageUpdateView.as_view(), name='package-update'),
    path('packages/delete/<int:pk>/', views.PackageDeleteView.as_view(), name='package-delete'),

    path('complain-types/', views.ComplainTypesListView.as_view(), name='complain-types-list'),
    path('complain-types/create/', views.ComplainTypesCreateView.as_view(), name='complain-types-create'),
    path('complain-types/update/<int:pk>/', views.ComplainTypesUpdateView.as_view(), name='complain-types-update'),
    path('complain-types/delete/<int:pk>/', views.ComplainTypesDeleteView.as_view(), name='complain-types-delete'),


]
