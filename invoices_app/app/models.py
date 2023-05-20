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
    number = models.IntegerField()
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.number