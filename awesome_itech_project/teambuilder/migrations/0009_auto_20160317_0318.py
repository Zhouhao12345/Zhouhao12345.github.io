# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0008_auto_20160316_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='merge_with',
            field=models.ForeignKey(to='teambuilder.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 17, 3, 18, 31, 865233)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 17, 3, 18, 31, 866933)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 17, 3, 18, 31, 865928)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=datetime.date(2016, 3, 17), null=True),
        ),
    ]
