# Generated by Django 5.1.1 on 2024-09-16 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_didikala', '0008_category_remove_clothes_product_category_and_more'),
        ('app_social', '0004_image_content_type_image_object_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
    ]
