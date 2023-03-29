from django.urls import path
from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]
