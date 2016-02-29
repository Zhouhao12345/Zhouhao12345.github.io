# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0030_remove_team_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberrequest',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]
