# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-16 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_expiration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('accept_application', 'Can accept applications'), ('invite_application', 'Can invite applications'), ('vote', 'Can invite applications'), ('checkin', 'Can mark as attended applications'), ('reject_application', 'Can reject applications'), ('force_status', 'Can force status application'))},
        ),
    ]
