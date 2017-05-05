# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_account_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=1024, unique=True),
        ),
    ]
