# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0017_auto_20160229_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberrequest',
            name='team',
            field=models.ForeignKey(default='', to='teambuilder.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 28, 3, 335179)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 28, 3, 334293)),
        ),
    ]
