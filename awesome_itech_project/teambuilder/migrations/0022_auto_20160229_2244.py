# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0021_auto_20160229_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 44, 5, 185189)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 44, 5, 187192)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 22, 44, 5, 189283)),
        ),
    ]
