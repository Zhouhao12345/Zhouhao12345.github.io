# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0008_auto_20160322_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 15, 33, 44, 607000)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 15, 33, 44, 607000)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 15, 33, 44, 607000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
