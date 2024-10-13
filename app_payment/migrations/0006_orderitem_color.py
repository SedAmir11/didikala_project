# Generated by Django 5.1 on 2024-10-06 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_didikala', '0030_alter_favorite_product'),
        ('app_payment', '0005_basketitem_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_didikala.color'),
        ),
    ]
