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
    return render(request, 'app/index.html', context)

def customer_detail(request, id):
    _customer = Customer.objects.get(id=id)
    form = CustomerForm(instance=_customer)
    context = {
        'site': 'customer',
        'form': form
    }
    return render(request, 'app/detail.html', context)

def material(request):
    context = {
        'site': 'material'
    }
    return render(request, 'app/index.html', context)

def company(request):
    context = {
        'site': 'company'
    }
    return render(request, 'app/index.html', context)

def invoice(request):
    context = {
        'site': 'invoice'
    }
    return render(request, 'app/index.html', context)