# Generated by Django 4.0 on 2022-01-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imag',
            field=models.ImageField(default='default.png', upload_to='static/profile_image'),
        ),
    ]
