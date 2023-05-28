from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('customer/', views.customer, name='customer'),
    path('customer/create', views.customer_create, name='customer_create'),
    path('customer/<int:_id>/change/', views.customer_form, name='customer_form'),
    path('customer/<int:_id>/', views.customer_detail, name='customer_detail'),

    path('material/', views.material, name='material'),
    path('material/create', views.material_create, name='material_create'),
    path('material/<int:_id>/', views.material_detail, name='material_detail'),
    path('material/<int:_id>/change/', views.material_form, name='material_form'),

    path('company/', views.company, name='company'),
    path('company/create', views.company_create, name='company_create'),
    path('company/<int:_id>/', views.company_detail, name='company_detail'),
    path('company/<int:_id>/change/', views.company_form, name='company_form'),

    path('invoice/', views.invoice, name='invoice'),

    path('contact_us', views.contact_us, name='contact_us'),
    path('email_sent', views.index, name='email_sent')
]