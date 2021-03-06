# Generated by Django 3.2.4 on 2021-08-18 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='if is valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='desc')),
                ('types', models.SmallIntegerField(default=10, help_text='10默认是首页轮播', verbose_name='type')),
                ('img', models.ImageField(max_length=256, upload_to='slider/%Y%m', verbose_name='img url')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='start time')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='end time')),
                ('reorder', models.SmallIntegerField(default=0, help_text='数字越大靠前', verbose_name='reorder')),
                ('target_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='link to')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
                'db_table': 'system_slider',
                'ordering': ['-reorder'],
            },
        ),
        migrations.CreateModel(
            name='ImageRelated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='if is valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('img', models.ImageField(max_length=256, upload_to='file/%Y%m', verbose_name='img url')),
                ('summary', models.CharField(blank=True, max_length=32, null=True, verbose_name='summary')),
                ('object_id', models.IntegerField(verbose_name='object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='model related')),
                ('user', models.ForeignKey(null=True, on_delete=models.SET(None), related_name='upload_images', to=settings.AUTH_USER_MODEL, verbose_name='who upload')),
            ],
            options={
                'verbose_name': 'ImageRelated',
                'verbose_name_plural': 'ImageRelated',
                'db_table': 'system_image_related',
            },
        ),
    ]
