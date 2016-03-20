# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import teambuilder.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0004_auto_20160320_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='dob',
        ),
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 20, 17, 36, 42, 554000)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 20, 17, 36, 42, 556000)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 20, 17, 36, 42, 555000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=b'default-avatar.jpg', upload_to=teambuilder.models.upload_location),
        ),
    ]
