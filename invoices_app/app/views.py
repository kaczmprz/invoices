from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Customer, Material, Company

# Create your views here.
def index(request):
    context = {
        'site': 'home'
    }
    return render(request, 'index.html', context)

def customer(request):
    customer_list = Customer.objects.order_by("-last_name")[:5]
    context = {
        'site': 'customer',
        'list': customer_list
    }
    return render(request, 'index.html', context)

def material(request):
    context = {
        'site': 'material'
    }
    return render(request, 'index.html', context)

def company(request):
    context = {
        'site': 'company'
    }
    return render(request, 'index.html', context)

def invoice(request):
    context = {
        'site': 'invoice'
    }
    return render(request, 'index.html', context)