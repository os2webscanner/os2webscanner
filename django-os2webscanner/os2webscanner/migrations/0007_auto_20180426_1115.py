# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-26 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('os2webscanner', '0006_auto_20180412_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filescanner',
            name='ciphertext',
        ),
        migrations.RemoveField(
            model_name='filescanner',
            name='iv',
        ),
        migrations.RemoveField(
            model_name='filescanner',
            name='username',
        ),
        migrations.RemoveField(
            model_name='webscanner',
            name='ciphertext',
        ),
        migrations.RemoveField(
            model_name='webscanner',
            name='iv',
        ),
        migrations.RemoveField(
            model_name='webscanner',
            name='username',
        ),
    ]
