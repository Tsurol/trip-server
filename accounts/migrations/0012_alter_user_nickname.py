# Generated by Django 3.2.4 on 2021-08-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210819_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=None, max_length=32, null=True, unique=True, verbose_name='nickname'),
        ),
    ]