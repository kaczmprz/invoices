from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from .models import Customer, Material, Company
from .forms import CustomerForm

# Create your views here.
def index(request):
    context = {
        'site': 'home'
    }
    return render(request, 'app/index.html', context)

def customer(request):
    customer_list = Customer.objects.order_by("-last_name")[:5]
    context = {
        'site': 'customer',
        'list': customer_list
    }
    return render(request, 'app/customer.html', context)

def customer_detail(request, id):
    _customer = Customer.objects.get(id=id)
    form = CustomerForm(instance=_customer)
    context = {
        'site': 'customer',
        'form': form
    }
    return render(request, 'app/customer_detail.html', context)

def material(request):
    material_list = Material.objects.all()
    context = {
        'site': 'material',
        'list': material_list
    }
    return render(request, 'app/material.html', context)

def material_detail(request, id):
    pass

def company(request):
    context = {
        'site': 'company'
    }
    return render(request, 'app/base.html', context)

def invoice(request):
    context = {
        'site': 'invoice'
    }
    return render(request, 'app/base.html', context)