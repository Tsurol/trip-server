# Generated by Django 3.2.4 on 2021-08-18 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_loginrecord_is_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='if_phone_valid',
            new_name='is_phone_valid',
        ),
    ]
