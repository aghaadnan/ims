from django.urls import path
from .views import (
    InventoryListView, InventoryDetailView, InventoryCreateView, InventoryUpdateView, InventoryDeleteView,
    TrackerDeviceListView,
    TrackerDeviceDetailView,
    TrackerDeviceCreateView,
    TrackerDeviceUpdateView,
    TrackerDeviceDeleteView,
    SimCreateView,
    SimListView,
    SimUpdateView,
    SimDeleteView
)
app_name = 'inventory'
urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory_list'),
    path('<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('new/', InventoryCreateView.as_view(), name='inventory_new'),
    path('<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory_edit'),
    path('<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),
    path('trackerdevices/', TrackerDeviceListView.as_view(), name='trackerdevice_list'),
    path('trackerdevices/new', TrackerDeviceCreateView.as_view(), name='trackerdevice_new'),
    path('trackerdevices/<int:pk>/edit/', TrackerDeviceUpdateView.as_view(), name='trackerdevice_edit'),
    path('trackerdevices/<int:pk>/delete/', TrackerDeviceDeleteView.as_view(), name='trackerdevice_delete'),
    path('trackerdevices/<int:pk>/', TrackerDeviceDetailView.as_view(), name='trackerdevice_detail'),
    path('sims/', SimListView.as_view(), name='sim_list'),
    path('sims/new', SimCreateView.as_view(), name='sim_new'),
    path('sims/<int:pk>/edit/', SimUpdateView.as_view(), name='sim_update'),
    path('sims/<int:pk>/delete/', SimDeleteView.as_view(), name='sim_delete'),
    #path('sims/<int:pk>/', SimDetailView.as_view(), name='sim_detail'),
]
