# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_auto_20150720_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='genome',
            field=models.ForeignKey(default='1', blank=True, to='viewer.Genome'),
            preserve_default=True,
        ),
    ]
