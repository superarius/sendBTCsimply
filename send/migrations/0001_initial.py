# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='pubtime')),
                ('tx', models.CharField(max_length=500)),
            ],
        ),
    ]
