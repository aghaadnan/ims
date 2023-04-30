from django.urls import path
from .views import (
    SalesLeadListView,
    SalesLeadCreateView,
    SalesLeadUpdateView,
    SalesLeadDeleteView,
)

app_name = "leads"

urlpatterns = [
    path("", SalesLeadListView.as_view(), name="sales-lead-list"),
    path("create/", SalesLeadCreateView.as_view(), name="sales-lead-create"),
    path("update/<int:pk>/", SalesLeadUpdateView.as_view(), name="sales-lead-update"),
    path("delete/<int:pk>/", SalesLeadDeleteView.as_view(), name="sales-lead-delete"),
]
