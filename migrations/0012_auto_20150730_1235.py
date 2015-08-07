# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0011_auto_20150723_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='bnid',
            field=models.ForeignKey(default=1, to='viewer.Bnid'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variant',
            name='sample',
            field=models.ForeignKey(default=1, to='viewer.Sample'),
            preserve_default=False,
        ),
    ]
