# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20160809_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(upload_to=''),
        ),
    ]
