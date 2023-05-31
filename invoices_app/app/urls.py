from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('customer/', views.customer, name='customer'),
    path('customer/create', views.customer_create, name='customer_create'),
    path('customer/<int:_id>/', views.customer_detail, name='customer_detail'),
    path('customer/<int:_id>/change/', views.customer_update, name='customer_update'),
    path('customer/<int:_id>/delete/', views.customer_delete, name='customer_delete'),

    path('material/', views.material, name='material'),
    path('material/create', views.material_create, name='material_create'),
    path('material/<int:_id>/', views.material_detail, name='material_detail'),
    path('material/<int:_id>/change/', views.material_update, name='material_update'),
    path('material/<int:_id>/delete/', views.material_delete, name='material_delete'),

    path('company/', views.company, name='company'),
    path('company/create', views.company_create, name='company_create'),
    path('company/<int:_id>/', views.company_detail, name='company_detail'),
    path('company/<int:_id>/change/', views.company_update, name='company_update'),
    path('company/<int:_id>/delete/', views.company_delete, name='company_delete'),

    path('invoice/', views.invoice, name='invoice'),
    path('invoice/create', views.invoice_create, name='invoice_create'),
    path('invoice/<int:_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoice/<int:_id>/change/', views.invoice_update, name='invoice_update'),
    path('invoice/<int:_id>/delete/', views.invoice_delete, name='invoice_delete'),
    path('invoice/<int:_id>/generate/', views.invoice_generate_pdf, name='invoice_generate'),

    path('contact_us', views.contact_us, name='contact_us'),
    path('email_sent', views.index, name='email_sent')
]