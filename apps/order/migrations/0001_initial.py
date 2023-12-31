# Generated by Django 3.2.8 on 2023-09-17 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0001_initial'),
        ('product', '__first__'),
        ('vendor', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('postal_code', models.CharField(max_length=50, verbose_name='Postcode')),
                ('address_line1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('address_line2', models.CharField(max_length=255, verbose_name='Address Line 2')),
                ('city', models.CharField(max_length=150, verbose_name='Town/City/State')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='OrderReciept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_quantity', models.CharField(max_length=250, null=True)),
                ('order_key', models.CharField(max_length=100, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('billing_status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('delivery_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_address_info', to='order.address', verbose_name='address info')),
                ('delivery_instructions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_delivery_info', to='checkout.deliveryoptions', verbose_name='delivery instructions')),
                ('payment_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_pay_option', to='checkout.paymentselections')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order Reciept',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderedItemDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.orderreciept')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='vendor.vendor')),
            ],
            options={
                'verbose_name_plural': 'Ordered Item Details',
                'ordering': ['-order'],
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_order', to='order.orderreciept')),
            ],
            options={
                'verbose_name_plural': 'Checkout',
                'ordering': ['-created'],
            },
        ),
    ]
