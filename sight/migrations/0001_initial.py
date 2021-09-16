# Generated by Django 3.2.4 on 2021-08-18 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='if is valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('desc', models.CharField(max_length=64, verbose_name='desc')),
                ('main_img', models.ImageField(max_length=512, upload_to='sight/%Y%m', verbose_name='main_img')),
                ('banner_img', models.ImageField(max_length=512, upload_to='sight/%Y%m', verbose_name='banner_img')),
                ('content', models.TextField(verbose_name='content')),
                ('score', models.FloatField(default=5, verbose_name='score')),
                ('province', models.CharField(max_length=32, verbose_name='province')),
                ('city', models.CharField(max_length=32, verbose_name='city')),
                ('area', models.CharField(blank=True, max_length=32, null=True, verbose_name='area')),
                ('town', models.CharField(blank=True, max_length=32, null=True, verbose_name='town')),
                ('min_price', models.FloatField(default=0, verbose_name='min_price')),
                ('is_top', models.BooleanField(default=False, verbose_name='is_top')),
                ('is_hot', models.BooleanField(default=False, verbose_name='is_hot')),
            ],
            options={
                'verbose_name': 'Sight',
                'verbose_name_plural': 'sight',
                'db_table': 'sight',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SightTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='if is valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('desc', models.CharField(blank=True, max_length=64, null=True, verbose_name='desc')),
                ('types', models.SmallIntegerField(choices=[(11, '成人票'), (12, '儿童票')], default=11, help_text='default adult ticket', verbose_name='types')),
                ('price', models.FloatField(verbose_name='original price')),
                ('discount', models.FloatField(default=10, verbose_name='discount')),
                ('total_stock', models.PositiveIntegerField(default=0, verbose_name='total stock')),
                ('remain_stock', models.PositiveIntegerField(default=0, verbose_name='remain stock')),
                ('expire_date', models.IntegerField(default=1, verbose_name='expire date')),
                ('return_policy', models.CharField(default='with condition', max_length=64, verbose_name='return policy')),
                ('has_invoice', models.BooleanField(default=True, verbose_name='if has invoice')),
                ('entry_way', models.SmallIntegerField(choices=[(0, '短信换票入园'), (1, '凭借验证码入园')], default=0, verbose_name='entry_way')),
                ('tips', models.TextField(blank=True, null=True, verbose_name='tips')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='remark')),
                ('status', models.SmallIntegerField(choices=[(1, '开放购买'), (0, '暂未开放')], default=1, verbose_name='状态')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to='sight.sight', verbose_name='Sight related')),
            ],
            options={
                'verbose_name': 'SightTicket',
                'verbose_name_plural': 'SightTicket',
                'db_table': 'sight_ticket',
            },
        ),
        migrations.CreateModel(
            name='SightInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_explain', models.CharField(blank=True, max_length=1024, null=True, verbose_name='entry_explain')),
                ('play_way', models.TextField(blank=True, null=True, verbose_name='play_types')),
                ('tips', models.TextField(blank=True, null=True, verbose_name='tips')),
                ('traffic', models.TextField(blank=True, null=True, verbose_name='traffic')),
                ('sight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='sight.sight', verbose_name='Sight related')),
            ],
            options={
                'verbose_name': 'SightInfo',
                'verbose_name_plural': 'SightInfo',
                'db_table': 'sight_info',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='if is valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('is_top', models.BooleanField(default=False, verbose_name='if is top')),
                ('love_count', models.IntegerField(default=0, verbose_name='love count')),
                ('score', models.FloatField(default=5, verbose_name='score')),
                ('ip_address', models.CharField(blank=True, max_length=64, null=True, verbose_name='ip address')),
                ('is_public', models.SmallIntegerField(default=1, verbose_name='if is public')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment', to='sight.comment', verbose_name='reply for comment')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sight.sight', verbose_name='sight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='commentator')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comment',
                'db_table': 'sight_comment',
                'ordering': ['-love_count', '-created_at'],
            },
        ),
    ]