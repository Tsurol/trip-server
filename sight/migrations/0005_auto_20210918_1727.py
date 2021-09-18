# Generated by Django 3.2.4 on 2021-09-18 09:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sight', '0004_sightticket_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sight',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='sightinfo',
            name='entry_explain',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1024, null=True, verbose_name='entry_explain'),
        ),
        migrations.AlterField(
            model_name='sightinfo',
            name='play_way',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='play_types'),
        ),
        migrations.AlterField(
            model_name='sightinfo',
            name='tips',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='tips'),
        ),
        migrations.AlterField(
            model_name='sightinfo',
            name='traffic',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='traffic'),
        ),
        migrations.AlterField(
            model_name='sightticket',
            name='remark',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='remark'),
        ),
        migrations.AlterField(
            model_name='sightticket',
            name='tips',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='tips'),
        ),
    ]
