# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_auto_20150515_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_file',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'Report File', blank=True),
            preserve_default=True,
        ),
    ]
