# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-04 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20200331_0456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='antique_id',
            new_name='antiques',
        ),
    ]
