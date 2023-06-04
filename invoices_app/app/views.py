from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.template import loader
from django.http import Http404, FileResponse
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import Customer, Material, Company, Invoice, Order
from .forms import CustomerForm, MaterialForm, CompanyForm, ContactUsForm, InvoiceForm, OrderFormSet
from reportlab.pdfgen import canvas

import io

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
            messages.success(request, 'Customer was updated successfully!')
            return redirect('app:customer_detail', _customer.id)
        else:
            messages.warning(request, 'Something went wrong')
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
            messages.success(request, 'Customer was created successfully!')
            return redirect('app:customer_detail', customer.id)
        else:
            messages.warning(request, 'Something went wrong')
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
            messages.success(request, 'Material was updated successfully!')
            return redirect('app:material_detail', _material.id)
        else:
            messages.warning(request, 'Something went wrong')
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
            messages.success(request, 'Customer was created successfully!')
            return redirect('app:material_detail', material.id)
        else:
            messages.warning(request, 'Something went wrong')
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
        messages.success(request, 'Material was deleted successfully!')
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
            messages.success(request, 'Company was updated successfully!')
            return redirect('app:company_detail', _company.id)
        else:
            messages.warning(request, 'Something went wrong')
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
            messages.success(request, 'Company was created successfully!')
            return redirect('app:company_detail', company.id)
        else:
            messages.warning(request, 'Something went wrong')
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
        messages.success(request, 'Company was deleted successfully!')
        return redirect('app:company')
    context = {
        'company': _company
    }
    return render(request, 'app/company_delete.html', context)

def invoice(request):
    invoice_list = Invoice.objects.all()
    context = {
        'list': invoice_list
    }
    return render(request, 'app/invoice.html', context)

def invoice_detail(request, _id):
    _invoice = get_object_or_404(Invoice, id=_id)
    context = {
        'item': _invoice
    }
    return render(request, 'app/invoice_detail.html', context)

'''
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            messages.success(request, 'Invoice was created successfully!')
            return redirect('app:invoice_detail', invoice.id)
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = InvoiceForm()
    context = {
        'form': form
    }
    return render(request, 'app/invoice_create.html', context)
'''

def invoice_create(request):
    invoice = Invoice()
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = OrderFormSet(request.POST, instance=invoice, prefix='children')
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            formset.save()
            messages.success(request, 'Invoice was created successfully!')
            return redirect('app:invoice_detail', invoice.id)
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = InvoiceForm(instance=invoice)
        formset = OrderFormSet(instance=invoice, prefix='children')
    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'app/invoice_create.html', context)

'''
def invoice_update(request, _id):
    _invoice = get_object_or_404(Invoice, id=_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=_invoice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Invoice was updated successfully!')
            return redirect('app:invoice_detail', _invoice.id)
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = InvoiceForm(instance=_invoice)
    context = {
        'form': form,
        'invoice_id': _invoice.id
    }
    return render(request, 'app/invoice_update.html', context=context)
'''
def invoice_update(request, _id):
    _invoice = get_object_or_404(Invoice, id=_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=_invoice)
        formset = OrderFormSet(request.POST, instance=_invoice, prefix='children')
        print(formset.errors)
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            formset.save()
            messages.success(request, 'Invoice was updated successfully!')
            return redirect('app:invoice_detail', _invoice.id)
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = InvoiceForm(instance=_invoice)
        formset = OrderFormSet(instance=_invoice, prefix='children')
    context = {
        'form': form,
        'formset': formset,
        'invoice_id': _invoice.id
    }
    return render(request, 'app/invoice_update.html', context=context)

def invoice_generate_pdf(request, _id):
    _invoice = get_object_or_404(Invoice, id=_id)
    context = {
        'invoice': _invoice
    }
    return render(request, 'app/pdf.html', context)


def invoice_delete(request, _id):
    _invoice = get_object_or_404(Invoice, id=_id)
    if request.method == 'POST':
        _invoice.delete()
        messages.success(request, 'Invoice was deleted successfully!')
        return redirect('app:invoice')
    context = {
        'invoice': _invoice
    }
    return render(request, 'app/invoice_delete.html', context)

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

