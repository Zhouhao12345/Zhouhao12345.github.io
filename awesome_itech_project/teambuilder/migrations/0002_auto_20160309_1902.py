# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 19, 2, 53, 111000)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 19, 2, 53, 113000)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 19, 2, 53, 112000)),
        ),
    ]
