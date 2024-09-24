# Generated by Django 5.1 on 2024-09-24 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_didikala', '0028_remove_specifications_category_description_product_and_more'),
        ('app_payment', '0002_alter_basket_item_product_alter_order_item_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='product',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.BooleanField(choices=[(False, 'failed'), (True, 'success')], default=False),
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_payment.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_didikala.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_payment.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_didikala.product')),
            ],
        ),
        migrations.DeleteModel(
            name='basket_item',
        ),
        migrations.DeleteModel(
            name='order_item',
        ),
    ]
