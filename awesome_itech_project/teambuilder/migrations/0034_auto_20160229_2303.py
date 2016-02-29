# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0033_team_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 23, 3, 10, 387129)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 23, 3, 10, 391586)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 23, 3, 10, 389191)),
            preserve_default=True,
        ),
    ]
