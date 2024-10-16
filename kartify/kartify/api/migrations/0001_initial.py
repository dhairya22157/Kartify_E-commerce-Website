# Generated by Django 5.0.1 on 2024-03-21 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('c_email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=127)),
                ('password', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('phone_num', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=31)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=31)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('s_email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=127)),
                ('phone_num', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order_contains_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_Agent',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=10)),
                ('d_email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_makes_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transaction_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('platform_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.DateTimeField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orders')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='s_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.seller'),
        ),
    ]
