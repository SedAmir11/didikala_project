# Generated by Django 5.1.1 on 2024-09-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_didikala', '0007_remove_image_banner_image_content_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='clothes_product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='digital_product',
            name='category',
        ),
        migrations.AddField(
            model_name='clothes_product',
            name='category',
            field=models.ManyToManyField(to='app_didikala.category'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='category',
            field=models.ManyToManyField(to='app_didikala.category'),
        ),
    ]
