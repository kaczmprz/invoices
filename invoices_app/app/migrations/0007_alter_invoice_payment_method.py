# Generated by Django 4.2.1 on 2023-06-03 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_invoice_payment_method_alter_invoice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'Cash'), ('BANK_TRANSFER', 'Bank transfer')], default='CASH', max_length=20, verbose_name='payment_method'),
        ),
    ]