# Generated by Django 5.1.1 on 2024-09-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_didikala', '0019_alter_productdetail_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
