# Generated by Django 4.1.7 on 2023-03-29 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='ShippingAddress',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='paymentMethod',
        ),
    ]