# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-17 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('os2webscanner', '0040_auto_20180711_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeScan',
            fields=[
                ('scan_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='os2webscanner.Scan')),
            ],
            options={
                'db_table': 'os2webscanner_exchangescan',
            },
            bases=('os2webscanner.scan',),
        ),
    ]
