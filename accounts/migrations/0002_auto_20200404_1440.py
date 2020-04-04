# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-04 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='', max_length=56),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='profile',
            name='post_code',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='profile',
            name='town',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]