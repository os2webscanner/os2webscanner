# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-17 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os2webscanner', '0045_auto_20180907_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='mime_type',
            field=models.CharField(max_length=256, null=True, verbose_name='Mime-type'),
        ),
    ]
