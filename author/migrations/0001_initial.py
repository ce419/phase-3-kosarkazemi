# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('std_num', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='user_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.User'),
        ),
    ]
