# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-26 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190121_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logging',
            name='client',
        ),
        migrations.DeleteModel(
            name='logging',
        ),
    ]
