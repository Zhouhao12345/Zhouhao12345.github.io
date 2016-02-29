# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teambuilder', '0029_auto_20160229_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='creator',
        ),
    ]
