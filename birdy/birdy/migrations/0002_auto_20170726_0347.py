# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birdy', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='birds',
            new_name='Bird',
        ),
    ]
