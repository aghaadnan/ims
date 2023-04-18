from django.urls import path
from . import views
app_name = 'companies'
urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('<int:pk>/', views.company_detail, name='company_detail'),
    path('new/', views.CompanyCreateView.as_view(), name='company_create'),
    path('<int:pk>/edit/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('<int:pk>/delete/', views.company_delete, name='company_delete'),
    path('toggle_company_status/', views.toggle_company_status, name='company_status_update'),
    path('email-templates/', views.EmailTemplateListView.as_view(), name='email_template_list'),
    path('email-templates/create/', views.EmailTemplateCreateView.as_view(), name='email_template_create'),
    path('email-templates/edit/<int:template_id>/', views.EmailTemplateUpdateView.as_view(), name='email_template_edit'),
    path('email-templates/delete/<int:template_id>/', views.EmailTemplateDeleteView.as_view(), name='email_template_delete'),
]
