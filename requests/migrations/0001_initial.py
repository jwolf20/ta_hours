# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
