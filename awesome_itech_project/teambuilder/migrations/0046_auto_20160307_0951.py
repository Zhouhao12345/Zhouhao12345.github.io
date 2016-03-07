# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0045_auto_20160229_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 7, 9, 51, 54, 35005)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 7, 9, 51, 54, 36666)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 9, 51, 54, 35884)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=datetime.date(2016, 3, 7), null=True),
        ),
    ]
