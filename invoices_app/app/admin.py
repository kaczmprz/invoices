from django.contrib import admin
from .models import Customer, Material, Company
# Register your models here.

admin.site.register(Customer)
admin.site.register(Material)
admin.site.register(Company)
