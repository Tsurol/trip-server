# Generated by Django 3.2.4 on 2021-08-18 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(editable=False, max_length=150, unique=True, verbose_name='username')),
                ('real_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='real name')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (0, '女')], default=1, verbose_name='sex')),
                ('age', models.SmallIntegerField(default=0, verbose_name='age')),
                ('email', models.CharField(blank=True, max_length=128, null=True, verbose_name='email')),
                ('is_email_valid', models.BooleanField(default=False, verbose_name='if email valid')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='phone number')),
                ('if_phone_valid', models.BooleanField(default=False, verbose_name='if phone valid')),
                ('source', models.CharField(blank=True, max_length=30, null=True, verbose_name='source')),
                ('version', models.CharField(blank=True, max_length=30, null=True, verbose_name='version')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User related')),
            ],
            options={
                'db_table': 'accounts_user_profile',
            },
        ),
        migrations.CreateModel(
            name='LoginRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='username')),
                ('ip', models.CharField(max_length=50, verbose_name='ip address')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('source', models.CharField(blank=True, max_length=30, null=True, verbose_name='source')),
                ('version', models.CharField(blank=True, max_length=30, null=True, verbose_name='version')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('is_valid', models.BooleanField(default=True, verbose_name='if is valid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User related')),
            ],
            options={
                'db_table': 'accounts_login_record',
            },
        ),
    ]