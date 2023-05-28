from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import Http404
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import Customer, Material, Company, Invoice
from .forms import CustomerForm, MaterialForm, CompanyForm, ContactUsForm

# Create your views here.
def index(request):
    num_customers = Customer.objects.all().count()
    num_materials = Material.objects.all().count()
    num_companies = Company.objects.all().count()
    num_invoices = Invoice.objects.all().count()

    context = {
        'site': 'home',
        'num_customers': num_customers,
        'num_materials': num_materials,
        'num_companies': num_companies,
        'num_invoices': num_invoices
    }
    return render(request, 'app/index.html', context)

def customer(request):
    customer_list = Customer.objects.order_by("-last_name")
    context = {
        'site': 'customer',
        'list': customer_list
    }
    return render(request, 'app/customer.html', context)

def customer_detail(request, _id):
    _customer = get_object_or_404(Customer, id=_id)
    context = {
        'site': 'customer',
        'item': _customer
    }
    return render(request, 'app/customer_detail.html', context)

def customer_form(request, _id):
    _customer = get_object_or_404(Customer, id=_id)
    form = CustomerForm(instance=_customer)
    context = {
        'site': 'customer',
        'form': form,
        'customer_id': _customer.id
    }
    return render(request, 'app/customer_form.html', context)

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('app:customer_detail', customer.id)
    else:
        form = CustomerForm()

    context = {
        'site': 'customer',
        'form': form,
    }
    return render(request, 'app/customer_create.html', context)


def material(request):
    material_list = Material.objects.all()
    context = {
        'site': 'material',
        'list': material_list
    }
    return render(request, 'app/material.html', context)

def material_detail(request, _id):
    _material = get_object_or_404(Material, id=_id)
    context = {
        'site': 'material',
        'item': _material
    }
    return render(request, 'app/material_detail.html', context)

def material_form(request, _id):
    _material = get_object_or_404(Material, id=_id)
    form = MaterialForm(instance=_material)
    context = {
        'site': 'material',
        'form': form,
        'material_id': _material.id
    }
    return render(request, 'app/material_form.html', context)

def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save()
            return redirect('app:material_detail', material.id)
    else:
        form = MaterialForm()
    context = {
        'form': form
    }
    return render(request, 'app/material_create.html', context)
def company(request):
    company_list = Company.objects.all()
    context = {
        'site': 'company',
        'list': company_list
    }
    return render(request, 'app/company.html', context)

def company_detail(request, _id):
    _company = get_object_or_404(Customer, id=_id)
    context = {
        'site': 'company',
        'item': _company
    }
    return render(request, 'app/company_detail.html', context)

def company_form(request, _id):
    _company = Company.objects.get(id=_id)
    form = CompanyForm(instance=_company)
    context = {
        'site': 'company',
        'form': form,
        'company_id': _company.id
    }
    return render(request, 'app/company_form.html', context)

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            return redirect('app:company_detail', company.id)
    else:
        form = CompanyForm()
    context = {
        'form': form
    }
    return render(request, 'app/company_create.html', context)

def invoice(request):
    context = {
        'site': 'invoice'
    }
    return render(request, 'app/base.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"]}',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@dupa.com']
            )
        return redirect('/email_sent')
    else:
        form = ContactUsForm()
    context = {
        'form': form
    }
    return render(request, 'app/contact_us.html', context=context)