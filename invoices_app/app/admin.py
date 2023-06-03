from django.contrib import admin
from .models import Customer, Material, Company, Invoice, Order
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

class OrderInline(admin.StackedInline):
    model = Order

    def get_parent_object_from_request(self, request):
        """
        Returns the parent object from the request or None.

        Note that this only works for Inlines, because the `parent_model`
        is not available in the regular admin.ModelAdmin as an attribute.
        """
        resolved = resolve(request.path_info)
        if resolved.args:
            return self.parent_model.objects.get(pk=resolved.kwargs["object_id"])
        return None

class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'customer',
        'company'
    )
    inlines = [OrderInline]



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Invoice, InvoiceAdmin)