# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_auto_20150720_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='genome',
            field=models.ForeignKey(default=1, blank=True, to='viewer.Genome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='aa_change',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Amino Acid Change', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='aa_length',
            field=models.IntegerField(null=True, verbose_name=b'Amino Acid Length', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='alt',
            field=models.CharField(max_length=256, null=True, verbose_name=b'Alternate Allele', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='coding',
            field=models.CharField(max_length=24, null=True, verbose_name=b'Coding', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='codon_change',
            field=models.CharField(max_length=16, null=True, verbose_name=b'Codon Change', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='context',
            field=models.CharField(max_length=512, null=True, verbose_name=b'Nuc Context', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='dbSnp_id',
            field=models.CharField(max_length=16, null=True, verbose_name=b'dbSnp ID', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='effect',
            field=models.CharField(max_length=32, null=True, verbose_name=b'Effect', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='gene_name',
            field=models.CharField(max_length=32, null=True, verbose_name=b'Gene Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='normal_alt_count',
            field=models.IntegerField(null=True, verbose_name=b'Normal Alt Count', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='normal_ref_count',
            field=models.IntegerField(null=True, verbose_name=b'Normal Ref Count', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='ref',
            field=models.CharField(max_length=256, null=True, verbose_name=b'Reference Allele', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='tumor_alt_count',
            field=models.IntegerField(null=True, verbose_name=b'Tumor Alt Count', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variant',
            name='tumor_ref_count',
            field=models.IntegerField(null=True, verbose_name=b'Tumor Ref Count', blank=True),
            preserve_default=True,
        ),
    ]
