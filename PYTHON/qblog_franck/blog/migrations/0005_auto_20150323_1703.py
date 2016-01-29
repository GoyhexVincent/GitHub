# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_entrys'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrys',
            new_name='Format',
        ),
    ]
