from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
import datetime
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
    vat_id = models.CharField(max_length=20)
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
    price = models.DecimalField(max_digits=38, decimal_places=2)

    def __str__(self):
        return self.desc

def invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
        return 1
    return last_invoice.number + 1

class Invoice(models.Model):

    class Meta:
        verbose_name_plural = _('Invoices')

    TYPE = Choices(
        ('INVOICE', _('Invoice')),
        ('PROFORMA', _('Proforma invoice')),
    )

    PAYMENT_METHOD = Choices(
        ('CASH', _('Cash')),
        ('BANK_TRANSFER', _('Bank transfer')),
    )

    number = models.IntegerField(default=invoice_number)
    sales_date = models.DateField(default=datetime.date.today)
    payment_date = models.DateField(default=datetime.date.today)
    payment_method = models.CharField(_('payment_method'), choices=PAYMENT_METHOD, default=PAYMENT_METHOD.CASH, max_length=20)
    type = models.CharField(_('type'), choices=TYPE, default=TYPE.INVOICE, max_length=20)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.number)

    def get_total_price(self):
        total = 0
        invoice = Invoice.objects.get(id=self.id)
        orders = invoice.order_set.all()
        for order in orders:
            total += order.get_total_item_price()
        return total




class Order(models.Model):
    material = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.invoice.id)

    def get_total_item_price(self):
        return self.quantity * self.material.price


