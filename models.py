from django.db import models


class Study(models.Model):
    name = models.CharField(max_length=64, verbose_name="Study Name")
    description = models.CharField(max_length=256,
                                   verbose_name="Study Description",
                                   blank=True)
    creation_date = models.DateTimeField('Date Created', auto_now=True,
                                         blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'studies'



class Caller(models.Model):
    name = models.CharField(max_length=64, verbose_name="Caller Name")

    def __str__(self):
        return self.name


class Genome(models.Model):
    name = models.CharField(max_length=64, verbose_name="Genome")

    def __str__(self):
        return self.name


class Sample(models.Model):
    name = models.CharField(max_length=48, verbose_name='Sample Name')
    description = models.CharField(max_length=256,
                                   verbose_name="Sample Description",
                                   blank=True)
    cellularity = models.CharField(max_length=8, verbose_name='% Cellularity',
                                   blank=True)
    study = models.ForeignKey(Study)
    creation_date = models.DateTimeField('Date Created', auto_now=True,
                                         blank=True)

    def __str__(self):
        return str(self.name)


class Bnid(models.Model):
    sample = models.ForeignKey(Sample)
    bnid = models.CharField(max_length=12, verbose_name='Bionimbus ID')
    description = models.CharField(max_length=256, verbose_name='Description',
                                   blank=True)
    creation_date = models.DateTimeField('Date Created', auto_now=True,
                                         blank=True)

    def __str__(self):
        return '{} ({})'.format(str(self.sample), str(self.bnid))


class Report(models.Model):
    caller = models.ForeignKey(Caller)
    study = models.ForeignKey(Study)
    genome = models.ForeignKey(Genome, default=1, blank=True)
    upload_date = models.DateTimeField('Date Uploaded', auto_now=True)
    bnids = models.ManyToManyField(Bnid, verbose_name='Bionimbus ID', blank=True)
    report_file = models.FileField('Report File', upload_to='', blank=True,
                                   null=True)

    def __str__(self):
        return str(self.report_file)


class Variant(models.Model):
    report = models.ForeignKey(Report)
    chrom = models.CharField(max_length=24, verbose_name='Chrom')
    pos = models.IntegerField(verbose_name='Position', null=True)
    ref = models.CharField(max_length=256, verbose_name='Reference Allele',
                           blank=True, null=True)
    alt = models.CharField(max_length=256, verbose_name='Alternate Allele',
                           blank=True, null=True)
    context = models.CharField(max_length=512, verbose_name='Nuc Context',
                               blank=True, null=True)
    normal_ref_count = models.IntegerField(verbose_name='Normal Ref Count',
                                           blank=True, null=True)
    normal_alt_count = models.IntegerField(verbose_name='Normal Alt Count',
                                           blank=True, null=True)
    tumor_ref_count = models.IntegerField(verbose_name='Tumor Ref Count',
                                          blank=True, null=True)
    tumor_alt_count = models.IntegerField(verbose_name='Tumor Alt Count',
                                          blank=True, null=True)
    dbSnp_id = models.CharField(max_length=16, verbose_name='dbSnp ID',
                                blank=True, null=True)
    gene_name = models.CharField(max_length=32, verbose_name='Gene Name',
                                 blank=True, null=True)
    effect = models.CharField(max_length=32, verbose_name='Effect',
                              blank=True, null=True)
    coding = models.CharField(max_length=24, verbose_name='Coding',
                              blank=True, null=True)
    codon_change = models.CharField(max_length=16, verbose_name='Codon Change',
                                    blank=True, null=True)
    amino_acid_change = models.CharField(max_length=16, null=True,
                                 verbose_name='Amino Acid Change', blank=True)
    amino_acid_length = models.IntegerField(verbose_name='Amino Acid Length',
                                            blank=True, null=True)

    def __str__(self):
        return "{}:{}{}>{}".format(self.chrom, self.pos, self.ref, self.alt)

