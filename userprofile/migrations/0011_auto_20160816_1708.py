# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20160816_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
