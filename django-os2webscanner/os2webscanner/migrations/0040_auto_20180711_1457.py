# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-11 12:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('os2webscanner', '0039_exchangedomain'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeScanner',
            fields=[
                ('scanner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='os2webscanner.Scanner')),
                ('domains', models.ManyToManyField(related_name='exchangedomains', to='os2webscanner.ExchangeDomain', verbose_name='Exchange Domæner')),
            ],
            options={
                'db_table': 'os2webscanner_exchangescanner',
            },
            bases=('os2webscanner.scanner',),
        ),
        migrations.AlterField(
            model_name='scan',
            name='columns',
            field=models.CharField(blank=True, max_length=128, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='columns',
            field=models.CharField(blank=True, max_length=128, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
