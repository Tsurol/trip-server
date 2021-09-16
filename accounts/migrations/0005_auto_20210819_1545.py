# Generated by Django 3.2.4 on 2021-08-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_if_phone_valid_profile_is_phone_valid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_email_valid',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_phone_valid',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=13000000000, max_length=20, unique=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
