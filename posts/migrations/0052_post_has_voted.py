# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0051_auto_20160905_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='has_voted',
            field=models.BooleanField(default=False),
        ),
    ]
