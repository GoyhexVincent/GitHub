# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_esp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Format',
            new_name='Postgres',
        ),
    ]
