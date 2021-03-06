# Generated by Django 3.2.4 on 2021-08-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=None, max_length=20, unique=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
