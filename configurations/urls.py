from django.urls import path
from . import views

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
]
