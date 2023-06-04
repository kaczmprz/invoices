import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoices_app.settings')
django.setup()

from faker import Faker
from app.models import Customer, Company, Material
import random


CUSTOMER_COUNT_OBJECTS = 10
COMPANY_COUNT_OBJECTS = 10
MATERIAL_COUNT_OBJECTS = 10
fake = Faker('pl_PL')

for i in range(CUSTOMER_COUNT_OBJECTS):
    customer = Customer()
    customer.first_name = fake.first_name()
    customer.last_name = fake.last_name()
    customer.address = fake.street_address()
    customer.city = fake.city()
    customer.country = fake.current_country()
    customer.save()

for i in range(COMPANY_COUNT_OBJECTS):
    company = Company()
    company.name = fake.company()
    company.vat_id = fake.msisdn()
    company.address = fake.street_address()
    company.city = fake.city()
    company.country = fake.current_country()
    company.save()

for i in range(MATERIAL_COUNT_OBJECTS):
    material = Material()
    material.number = fake.ean8(prefixes=('45', '49'))
    material.desc = 'Mat-' + str(material.number)
    material.category = random.choice(['FO', 'BG', 'CG', 'ND'])
    material.price = fake.pyfloat(positive=True, min_value=1, max_value=100)
    material.save()


