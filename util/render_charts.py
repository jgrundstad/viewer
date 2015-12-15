__author__ = 'Dominic Fitzgerald'
import simplejson
import random
from viewer.models import Report, Study, Sample
from report_parser import parse_extra_info


def effectratio(**kwargs):
    reports = Report.objects.filter(pk__in=kwargs['reportId'])

    effect_ratio_dict = {}
    for report in reports:
        for variant in report.variant_set.all():
            effect = parse_extra_info(variant)['effect']
            if effect not in effect_ratio_dict.keys():
                effect_ratio_dict[effect] = 0
            effect_ratio_dict[effect] += 1

    chart_title = 'Effect Ratio: ' + ', '.join([report.name for report in reports])

    chart = {
        'chart': {
            'type': 'pie'
        },
        'title': {
            'text': chart_title
        },
        'series': [
            {
                'name': 'Effect',
                'data': [
                    {'name': elem, 'y': effect_ratio_dict[elem]} for elem in effect_ratio_dict
                ]
            }

        ]
    }
    return chart


def topfivegenes(**kwargs):
    reports = Report.objects.filter(pk__in=kwargs['reportId'])

    gene_dict = {}
    for report in reports:
        for variant in report.variant_set.all():
            gene_name = variant.gene_name
            if gene_name not in gene_dict.keys():
                gene_dict[gene_name] = 0
            gene_dict[gene_name] += 1
    del gene_dict['']

    top_five_genes = sorted(gene_dict, key=gene_dict.__getitem__, reverse=True)[:5]

    chart_title = 'Top Five Gene Occurrences: ' + ', '.join([report.name for report in reports])

    chart = {
        'chart': {
            'type': 'column'
        },
        'title': {
            'text': chart_title
        },
        'xAxis': {
            'categories': top_five_genes
        },
        'yAxis': {
            'title': {
                'text': 'Number of Occurrences'
            }
        },
        'series': [
            {
                'name': 'Genes',
                'data': [gene_dict[t] for t in top_five_genes]
            }

        ]
    }
    return chart


def refalleleratio(**kwargs):
    report = Report.objects.get(pk=kwargs['reportId'])

    alleles = [0, 0, 0, 0]
    for variant in report.variant_set.all():
        variant_ref = variant.ref
        if variant_ref == 'A':
            alleles[0] += 1
        elif variant_ref == 'C':
            alleles[1] += 1
        elif variant_ref == 'G':
            alleles[2] += 1
        elif variant_ref == 'T':
            alleles[3] += 1

    chart = {
        'chart': {
            'type': 'pie'
        },
        'title': {
            'text': 'Ref Allele Frequency'
        },
        'series': [
            {
                'name': 'Ref',
                'data': [
                    {'name': 'A', 'y': alleles[0]},
                    {'name': 'C', 'y': alleles[1]},
                    {'name': 'G', 'y': alleles[2]},
                    {'name': 'T', 'y': alleles[3]}
                ]
            }

        ]
    }
    return chart


def qualitative_map(**kwargs):
    reports = Report.objects.filter(pk__in=kwargs['reportId'])

    # sample_ids = []
    # for report in reports:
    #     samples = report.study.sample_set.all()
    #     for sample in samples:
    #         if sample.pk not in sample_ids:
    #             sample_ids.append(sample.pk)
    # samples = Sample.objects.filter(pk__in=sample_ids)
    # genes = ['CSMD1', 'CNTN5', 'RBFOX1', 'PCDH15', 'RIMS2']
    #
    # data = []
    # for i, gene in enumerate(genes):
    #     for j, sample in enumerate(samples):
    #         variant_present = 0
    #
    #         data.append([i, j, random.randint(0, 1)])

    gene_dict = {}
    for report in reports:
        for variant in report.variant_set.all():
            gene_name = variant.gene_name
            if gene_name not in gene_dict.keys():
                gene_dict[gene_name] = 0
            gene_dict[gene_name] += 1
    del gene_dict['']

    top_five_genes = sorted(gene_dict, key=gene_dict.__getitem__, reverse=True)[:5]
    genes_hot_list = ['KRAS', 'PIK3CA', 'TP53', 'GNAS', 'DCC']

    genes = top_five_genes + [gene for gene in genes_hot_list if gene not in top_five_genes]
    data = []
    for i, gene in enumerate(genes):
        for j, report in enumerate(reports):
            variant_present = 1 if report.variant_set.filter(gene_name__iexact=gene).count() > 0 else 0
            data.append([i, j, variant_present])

    chart = {
        'chart': {
            'type': 'heatmap',
            'plotBorderWidth': '1'
        },
        'colors': ['#003459'],
        'title': {
            'text': 'Variant status across selected reports'
        },
        'xAxis': {
            'categories': genes,
            'opposite': True

        },
        'yAxis': {
            'categories': [report.name + '<br/>Tumor Sample' for report in reports],
            'title': {
                'text': 'Samples'
            }
        },
        'colorAxis': {
            'min': 0,
            'max': 1,
            'minColor': '#FFFFFF',
            'maxColor': '#003459'
        },
        'legend': {
           'enabled': False
        },
        'tooltip': {
           'enabled': False
        },
        'series': [
            {
                'borderWidth': '4',
                'borderColor': '#EDEDED',
                'data': data
                #     [0,0,10], [0,1,3], [0,2,4],
                #     [1,0,5], [1,1,3], [1,2,8],
                #     [2,0,8], [2,1,4], [2,2,9],
                #     [3,0,12], [3,1,1], [3,2,3],
                #     [4,0,13], [4,1,0], [4,2,6]
                # ]
            }

        ]
    }
    return chart
