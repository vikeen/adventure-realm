# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0004_auto_20170420_1830'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='summaryparagraph',
            table='summary_paragraph',
        ),
        migrations.AlterModelTable(
            name='summarysentence',
            table='summary_sentence',
        ),
    ]