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
    price = models.FloatField()

    def __str__(self):
        return self.desc

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

    number = models.IntegerField()
    sales_date = models.DateField()
    payment_date = models.DateField()
    payment_method = models.CharField(_('payment_method'), choices=PAYMENT_METHOD, default=PAYMENT_METHOD.CASH, max_length=20)
    type = models.CharField(_('type'), choices=TYPE, default=TYPE.INVOICE, max_length=20)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    #material = models.ManyToManyField(Material)
    #order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.number)


class Order(models.Model):
    material = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.invoice.id)

    def get_total_item_price(self):
        return self.quantity * self.material.price
