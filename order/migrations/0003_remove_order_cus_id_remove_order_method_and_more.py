# Generated by Django 4.0.2 on 2022-04-23 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_brand_alter_category_options_and_more'),
        ('vendor', '0002_remove_vendor_created_by_vendor_email_and_more'),
        ('order', '0002_rename_first_name_order_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cus_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='method',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product_name',
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='vendors',
            field=models.ManyToManyField(default=None, related_name='orders', to='vendor.Vendor'),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='vendor.vendor'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8),
        ),
    ]
