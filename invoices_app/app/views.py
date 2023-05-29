from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
        'num_customers': num_customers,
        'num_materials': num_materials,
        'num_companies': num_companies,
        'num_invoices': num_invoices
    }
    return render(request, 'app/index.html', context)

def customer(request):
    customer_list = Customer.objects.order_by("-last_name")
    context = {
        'list': customer_list
    }
    return render(request, 'app/customer.html', context)

def customer_detail(request, _id):
    _customer = get_object_or_404(Customer, id=_id)
    context = {
        'item': _customer
    }
    return render(request, 'app/customer_detail.html', context)

def customer_update(request, _id):
    _customer = get_object_or_404(Customer, id=_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=_customer)
        if form.is_valid():
            form.save()
            return redirect('app:customer_detail', _customer.id)
        else:
            messages.warning(request, 'Something went wrong', extra_tags='alert')
    else:
        form = CustomerForm(instance=_customer)

    context = {
        'form': form,
        'customer_id': _customer.id
    }
    return render(request, 'app/customer_update.html', context)

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('app:customer_detail', customer.id)
    else:
        form = CustomerForm()

    context = {
        'form': form,
    }
    return render(request, 'app/customer_create.html', context)

def customer_delete(request, _id):
    _customer = get_object_or_404(Customer, id=_id)
    if request.method == 'POST':
        _customer.delete()
        messages.success(request, 'Customer was deleted successfully!')
        return redirect('app:customer')

    context = {
        'customer': _customer,
    }
    return render(request, 'app/customer_delete.html', context)


def material(request):
    material_list = Material.objects.all()
    context = {
        'list': material_list
    }
    return render(request, 'app/material.html', context)

def material_detail(request, _id):
    _material = get_object_or_404(Material, id=_id)
    context = {
        'item': _material
    }
    return render(request, 'app/material_detail.html', context)

def material_update(request, _id):
    _material = get_object_or_404(Material, id=_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=_material)
        if form.is_valid():
            form.save()
            return redirect('app:material_detail', _material.id)
    else:
        form = MaterialForm(instance=_material)
    context = {
        'form': form,
        'material_id': _material.id
    }
    return render(request, 'app/material_update.html', context)

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


def material_delete(request, _id):
    _material = get_object_or_404(Material, id=_id)
    if request.method == 'POST':
        _material.delete()
        return redirect('app:material')
    context = {
        'material': _material,
    }
    return render(request, 'app/material_delete.html', context)


def company(request):
    company_list = Company.objects.all()
    context = {
        'list': company_list
    }
    return render(request, 'app/company.html', context)

def company_detail(request, _id):
    _company = get_object_or_404(Company, id=_id)
    context = {
        'item': _company
    }
    return render(request, 'app/company_detail.html', context)

def company_update(request, _id):
    _company = Company.objects.get(id=_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=_company)
        if form.is_valid():
            form.save()
            return redirect('app:company_detail', _company.id)
    else:
        form = CompanyForm(instance=_company)
    context = {
        'form': form,
        'company_id': _company.id
    }
    return render(request, 'app/company_update.html', context)

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

def company_delete(request, _id):
    _company = get_object_or_404(Company, id=_id)
    if request.method == 'POST':
        _company.delete()
        return redirect('app:company')
    context = {
        'company': _company
    }
    return render(request, 'app/company_delete.html', context)

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