from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return " ".join([self.first_name, self.last_name])


class Company(models.Model):
    name = models.CharField(max_length=50)
    vat_id = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
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
    number = models.IntegerField()
    sale_date = models.DateField()
    payment_date = models.DateField()
    seller = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    buyer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.number)

    def pdf(self):
        pass