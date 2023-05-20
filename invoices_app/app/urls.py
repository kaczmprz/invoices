from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer, name='customer'),
    path('customer/<int:id>/', views.customer_detail, name='customer_detail'),
    path('material/', views.material, name='material'),
    path('company/', views.company, name='company'),
    path('invoice/', views.invoice, name='invoice'),
]