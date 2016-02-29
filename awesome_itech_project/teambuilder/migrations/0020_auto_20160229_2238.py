# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0019_auto_20160229_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_password',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='course',
            name='team_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 38, 42, 307337)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 38, 42, 306661)),
        ),
    ]
