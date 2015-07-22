# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0009_auto_20150721_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='aa_change',
            new_name='amino_acid_change',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='aa_length',
            new_name='amino_acid_length',
        ),
    ]
