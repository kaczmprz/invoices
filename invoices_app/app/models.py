from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
# Create your models here.
class Customer(models.Model):

    class Meta:
        verbose_name_plural = _('Customers')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return " ".join([self.first_name, self.last_name])


class Company(models.Model):

    class Meta:
        verbose_name_plural = _('Companies')

    name = models.CharField(max_length=50)
    vat_id = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):

    class Meta:
        verbose_name_plural = _('Materials')

    class Category(models.TextChoices):
        FOOD = 'FO'
        BEVERAGES = 'BG'
        CIGGARETES = 'CG'
        NO_DATA = 'ND'

    number = models.IntegerField()
    desc = models.CharField(max_length=100)
    category = models.CharField(choices=Category.choices, max_length=4, default='ND')

    def __str__(self):
        return self.desc


class Invoice(models.Model):

    class Meta:
        verbose_name_plural = _('Invoices')

    TYPE = Choices(
        ('INVOICE', _('Invoice')),
        ('PROFORMA', _('Proforma invoice')),
    )

    number = models.IntegerField()
    sales_date = models.DateField()
    payment_date = models.DateField()
    type = models.CharField(_('status'), choices=TYPE, default=TYPE.INVOICE, max_length=20)
    customer = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    material = models.ManyToManyField(Material)

    def __str__(self):
        return str(self.number)

    def pdf(self):
        pass