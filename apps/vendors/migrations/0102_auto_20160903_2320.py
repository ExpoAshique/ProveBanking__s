# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-03 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0101_auto_20160702_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='certverification',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to='certs/'),
        ),
        migrations.AddField(
            model_name='certverification',
            name='date_awarded',
            field=models.DateField(blank=True, null=True),
        ),
    ]
