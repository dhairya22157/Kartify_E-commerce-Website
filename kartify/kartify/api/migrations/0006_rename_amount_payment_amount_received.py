# Generated by Django 5.0.1 on 2024-04-25 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_amount_received_payment_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='amount',
            new_name='amount_received',
        ),
    ]
