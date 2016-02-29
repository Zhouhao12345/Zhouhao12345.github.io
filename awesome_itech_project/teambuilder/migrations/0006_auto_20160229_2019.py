# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0005_auto_20160229_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='aboutme',
            new_name='about_me',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phonenumber',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 20, 19, 45, 417131)),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 20, 19, 45, 416125)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 20, 19, 45, 418824)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 20, 19, 45, 415517)),
        ),
    ]
