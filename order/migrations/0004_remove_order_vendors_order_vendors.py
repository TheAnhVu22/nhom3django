# Generated by Django 4.0.2 on 2022-04-23 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_cus_id_remove_order_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='vendors',
        ),
        migrations.AddField(
            model_name='order',
            name='vendors',
            field=models.CharField(default=None, max_length=100),
        ),
    ]