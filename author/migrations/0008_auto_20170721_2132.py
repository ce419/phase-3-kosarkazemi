# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0007_auto_20170721_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, default='NO Title', max_length=100, null=True),
        ),
    ]