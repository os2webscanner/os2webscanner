# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-31 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os2webscanner', '0043_exchangescan_folder_to_scan'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangescan',
            name='mark_scan_as_done',
            field=models.BooleanField(default=False),
        ),
    ]
