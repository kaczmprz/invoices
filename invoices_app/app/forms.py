from django import forms
from django.forms import inlineformset_factory, formset_factory
from .models import Customer, Material, Company, Invoice, Order

class CustomerForm(forms.ModelForm):
   class Meta:
     model = Customer
     fields = '__all__'

class MaterialForm(forms.ModelForm):
   class Meta:
     model = Material
     fields = '__all__'

class CompanyForm(forms.ModelForm):
   class Meta:
     model = Company
     fields = '__all__'

class OrderForm(forms.ModelForm):
   class Meta:
     model = Order
     fields = '__all__'


class InvoiceForm(forms.ModelForm):
   class Meta:
     model = Invoice
     fields = '__all__'
'''
   material = forms.ModelMultipleChoiceField(
       queryset=Material.objects.all(),
       widget=forms.CheckboxSelectMultiple
   )
'''

OrderFormSet = inlineformset_factory(Invoice, Order, form=OrderForm, extra=1)

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=100)