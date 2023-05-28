from django import forms
from .models import Customer, Material, Company

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