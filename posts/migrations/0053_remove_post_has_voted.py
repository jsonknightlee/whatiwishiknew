# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 22:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0052_post_has_voted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='has_voted',
        ),
    ]
