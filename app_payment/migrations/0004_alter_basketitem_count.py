# Generated by Django 5.1 on 2024-09-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_payment', '0003_remove_order_item_order_remove_order_item_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
