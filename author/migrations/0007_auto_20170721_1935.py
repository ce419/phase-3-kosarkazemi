# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_blog_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='token',
            new_name='title',
        ),
    ]
