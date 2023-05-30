from django.contrib import admin
from .models import Customer, Material, Company, Invoice
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name'
    )

class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'vat_id'
    )

class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'desc'
    )

class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'customer',
        'company'
    )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Invoice, InvoiceAdmin)