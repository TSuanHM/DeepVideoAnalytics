# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0025_auto_20170309_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexentries',
            name='framelist',
        ),
    ]
