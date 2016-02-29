# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0031_auto_20160229_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberrequest',
            name='status',
            field=models.CharField(default=b'pending', max_length=10),
        ),
    ]
