# Generated by Django 4.2.1 on 2023-06-04 08:39

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_company_vat_id_alter_material_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(default=app.models.invoice_number),
        ),
    ]