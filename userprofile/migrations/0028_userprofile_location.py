# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0027_auto_20160905_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='City', max_length=50),
        ),
    ]
