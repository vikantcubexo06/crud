# Generated by Django 4.0 on 2022-01-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imag',
            field=models.ImageField(default='default.png', upload_to='profile_image'),
        ),
    ]
