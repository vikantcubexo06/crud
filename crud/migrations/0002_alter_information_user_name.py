# Generated by Django 4.0 on 2022-01-13 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='User_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
