# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0025_auto_20160904_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='user biography', max_length=100),
        ),
    ]
