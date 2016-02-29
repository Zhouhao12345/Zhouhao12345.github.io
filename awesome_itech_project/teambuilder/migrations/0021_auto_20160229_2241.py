# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0020_auto_20160229_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='creation_date',
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 41, 31, 70041)),
        ),
    ]
