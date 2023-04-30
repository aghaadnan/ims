"""IMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import redirect_user, LandingPageView
from dashboards.views import DashboardView


admin.site.site_header = "Tracker MIS Admin"
admin.site.site_title = "Tracker MIS Admin Portal"
admin.site.index_title = "Welcome to Tracker MIS Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('companies/', include('companies.urls', namespace='home')),
    path('inventory/', include('inventory.urls', namespace="inventory")),
    path('customers/', include('customers.urls', namespace="cusotmers")),
    path('vehicles/', include('vehicles.urls', namespace="vehicles")),
    path('installations/', include('installations.urls', namespace="installations")),
   # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboards/',include('dashboards.urls', namespace="dashboards")),
    path('configurations/',include('configurations.urls', namespace="configurations")),
    path('leads/',include('leads.urls', namespace="leads")),
    path('redirect/', redirect_user, name='redirect'),
    
]
