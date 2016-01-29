# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150506_1550'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Esp',
            new_name='NSFW',
        ),
    ]
