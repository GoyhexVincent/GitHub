# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='house4sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=50, verbose_name=b'Owner of the house')),
                ('price', models.IntegerField(verbose_name=b'Price in $', blank=True)),
                ('area', models.IntegerField(verbose_name=b'House area [m2]', blank=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Houses for sale',
            },
            bases=(models.Model,),
        ),
    ]
