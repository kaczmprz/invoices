from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer', views.customer, name='customer'),
    path('material', views.material, name='material'),
    path('company', views.company, name='company'),
    path('invoice', views.invoice, name='invoice'),
]