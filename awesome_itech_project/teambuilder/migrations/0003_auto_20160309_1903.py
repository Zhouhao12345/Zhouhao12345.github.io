# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0002_auto_20160309_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 19, 3, 56, 577000)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 19, 3, 56, 579000)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 19, 3, 56, 578000)),
        ),
    ]
