# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_auto_20150518_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'Genome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chrom', models.CharField(max_length=24, verbose_name=b'Chrom')),
                ('pos', models.IntegerField(verbose_name=b'Position')),
                ('ref', models.CharField(max_length=256, verbose_name=b'Reference Allele', blank=True)),
                ('alt', models.CharField(max_length=256, verbose_name=b'Alternate Allele', blank=True)),
                ('context', models.CharField(max_length=512, verbose_name=b'Nuc Context', blank=True)),
                ('normal_ref_count', models.IntegerField(verbose_name=b'Normal Ref Count', blank=True)),
                ('normal_alt_count', models.IntegerField(verbose_name=b'Normal Alt Count', blank=True)),
                ('tumor_ref_count', models.IntegerField(verbose_name=b'Tumor Ref Count', blank=True)),
                ('tumor_alt_count', models.IntegerField(verbose_name=b'Tumor Alt Count', blank=True)),
                ('dbSnp_id', models.CharField(max_length=16, verbose_name=b'dbSnp ID', blank=True)),
                ('gene_name', models.CharField(max_length=32, verbose_name=b'Gene Name', blank=True)),
                ('effect', models.CharField(max_length=32, verbose_name=b'Effect', blank=True)),
                ('coding', models.CharField(max_length=24, verbose_name=b'Coding', blank=True)),
                ('codon_change', models.CharField(max_length=16, verbose_name=b'Codon Change', blank=True)),
                ('aa_change', models.CharField(max_length=16, verbose_name=b'Amino Acid Change', blank=True)),
                ('aa_length', models.IntegerField(verbose_name=b'Amino Acid Length', blank=True)),
                ('report', models.ForeignKey(to='viewer.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='genome',
            field=models.ForeignKey(default=1, blank=True, to='viewer.Genome'),
            preserve_default=False,
        ),
    ]
