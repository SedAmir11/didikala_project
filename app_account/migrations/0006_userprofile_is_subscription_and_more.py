# Generated by Django 5.1.1 on 2024-09-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0005_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_Subscription',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='usersimage'),
        ),
    ]
