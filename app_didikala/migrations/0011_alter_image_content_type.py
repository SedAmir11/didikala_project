# Generated by Django 5.1.1 on 2024-09-16 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_didikala', '0010_alter_image_content_type_alter_image_image'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_didikala_images', to='contenttypes.contenttype'),
        ),
    ]
