# from django.urls import path
# from .views import TrackerInstallationCreateView

# app_name = 'installations'

# urlpatterns = [
#     path('tracker-installation/create/', TrackerInstallationCreateView.as_view(), name='tracker_installation_create'),
# ]
from django.urls import path
from .views import (
    TrackerInstallationListView,
    TrackerInstallationCreateView,
    TrackerInstallationUpdateView,
    TrackerInstallationDeleteView
)

app_name = 'installations'

urlpatterns = [
    path('', TrackerInstallationListView.as_view(), name='tracker-installation-list'),
    path('create/', TrackerInstallationCreateView.as_view(), name='trackerinstallation_create'),
    path('<int:pk>/update/', TrackerInstallationUpdateView.as_view(), name='trackerinstallation_update'),
    path('<int:pk>/delete/', TrackerInstallationDeleteView.as_view(), name='trackerinstallation_delete'),
]
