# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-12 19:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('antiques', '0005_auto_20200412_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
