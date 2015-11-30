from django.contrib import admin
from models import Project, Bnid, Sample, Study, Caller, Report, Variant, \
    Genome, Contact, SharedData


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('id', 'name', 'description', 'creation_date')
    filter_horizontal = ('user', )


class BnidAdmin(admin.ModelAdmin):
    model = Bnid


class SampleAdmin(admin.ModelAdmin):
    model = Sample
    list_display =('id', 'name')


class CallerAdmin(admin.ModelAdmin):
    display = ['name']


class ReportAdmin(admin.ModelAdmin):
    model = Report
    list_display = ('caller', 'report_file', 'upload_date')


class StudyAdmin(admin.ModelAdmin):
    model = Study
    list_display = ('name', 'description')


class GenomeAdmin(admin.ModelAdmin):
    model = Genome
    list_display = ('id', 'name')


class VariantAdmin(admin.ModelAdmin):
    model = Variant
    list_display = ('__str__', 'report', 'gene_name', 'chrom', 'pos', 'ref', 'alt',
                    'normal_ref_count', 'normal_alt_count', 'tumor_ref_count',
                    'tumor_alt_count')

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('full_name', 'email', 'project')

class SharedDataAdmin(admin.ModelAdmin):
    model = SharedData
    list_display = ('uuid', 'field_lookup', 'user', 'creation_date', 'inactive_date')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Bnid, BnidAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Caller, CallerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Genome, GenomeAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SharedData, SharedDataAdmin)