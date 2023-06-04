from django.urls import path
from . import views

urlpatterns = [
    path('api/customer', views.customer, name='customer'),
    path('api/material', views.material, name='material'),
    path('api/company', views.company, name='company'),
    path('api/invoice', views.invoice, name='invoice'),
]
