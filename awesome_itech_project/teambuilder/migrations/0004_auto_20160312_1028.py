# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0003_auto_20160309_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 10, 28, 57, 99235)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 10, 28, 57, 100903)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 10, 28, 57, 99980)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=datetime.date(2016, 3, 12), null=True),
        ),
    ]
