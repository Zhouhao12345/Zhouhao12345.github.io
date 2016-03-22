# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0006_auto_20160320_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile_skill',
            name='skill',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.RemoveField(
            model_name='userprofile_skill',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='UserProfile_Skill',
        ),
        migrations.AlterField(
            model_name='course',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 9, 20, 23, 143000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='team_size',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='memberrequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 9, 20, 23, 146000)),
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 9, 20, 23, 144000)),
        ),
    ]
