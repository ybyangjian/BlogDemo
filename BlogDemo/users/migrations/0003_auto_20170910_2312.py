# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170910_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]