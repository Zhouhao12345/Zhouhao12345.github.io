# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0028_auto_20160229_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='memberrequest',
            name='request_date',
        ),
        migrations.RemoveField(
            model_name='team',
            name='creation_date',
        ),
    ]
