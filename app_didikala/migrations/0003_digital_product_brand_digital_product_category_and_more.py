# Generated by Django 5.1.1 on 2024-09-16 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_didikala', '0002_image_url'),
        ('app_social', '0002_alter_category_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='digital_product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_didikala.brand'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digital_categories', to='app_social.category'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='images',
            field=models.ManyToManyField(null=True, to='app_social.image'),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='digital_product',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='field',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='clothes_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('count', models.PositiveIntegerField(null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_didikala.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clothes_categories', to='app_social.category')),
                ('images', models.ManyToManyField(null=True, to='app_social.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
