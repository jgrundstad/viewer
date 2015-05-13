# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_auto_20150512_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='cellularity',
            field=models.CharField(max_length=8, verbose_name=b'% Cellularity', blank=True),
            preserve_default=True,
        ),
    ]
