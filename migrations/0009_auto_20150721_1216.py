# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_auto_20150721_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='pos',
            field=models.IntegerField(null=True, verbose_name=b'Position'),
            preserve_default=True,
        ),
    ]
