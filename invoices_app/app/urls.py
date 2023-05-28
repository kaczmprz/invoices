from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('customer/', views.customer, name='customer'),
    path('customer/<int:_id>/change/', views.customer_form, name='customer_form'),
    path('customer/<int:_id>/', views.customer_detail, name='customer_detail'),

    path('material/', views.material, name='material'),
    path('material/<int:_id>/', views.material_detail, name='material_detail'),
    path('material/<int:_id>/change/', views.material_form, name='material_form'),

    path('company/', views.company, name='company'),
    path('company/<int:_id>/', views.company_detail, name='company_detail'),
    path('company/<int:_id>/change/', views.company_form, name='company_form'),

    path('invoice/', views.invoice, name='invoice'),
]