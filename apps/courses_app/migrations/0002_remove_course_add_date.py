# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 04:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='add_date',
        ),
    ]
