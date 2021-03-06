# Generated by Django 3.2.4 on 2021-08-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210820_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginrecord',
            name='ip',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ip address'),
        ),
        migrations.AlterField(
            model_name='loginrecord',
            name='username',
            field=models.CharField(editable=False, max_length=150, unique=True, verbose_name='username'),
        ),
    ]
