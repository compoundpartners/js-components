# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-02 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_components', '0009_counter_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='body',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]
