# Generated by Django 4.1.3 on 2023-01-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_invoice_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceproduct',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]