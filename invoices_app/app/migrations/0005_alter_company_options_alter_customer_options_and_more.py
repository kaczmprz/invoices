# Generated by Django 4.2.1 on 2023-06-03 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_buyer_invoice_company_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'Materials'},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.company'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer'),
        ),
    ]
