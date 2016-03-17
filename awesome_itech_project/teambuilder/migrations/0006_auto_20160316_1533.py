# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0005_auto_20160312_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 15, 33, 4, 615000)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 15, 33, 4, 617000)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 15, 33, 4, 616000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=datetime.date(2016, 3, 16), null=True),
        ),
    ]
