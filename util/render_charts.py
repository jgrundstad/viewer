__author__ = 'Dominic Fitzgerald'
from viewer.models import Report
from report_parser import parse_extra_info


def effectratio(**kwargs):
    report = Report.objects.get(pk=kwargs['reportId'])

    effect_ratio_dict = {}
    for variant in report.variant_set.all():
        effect = parse_extra_info(variant)['effect']
        if effect not in effect_ratio_dict.keys():
            effect_ratio_dict[effect] = 0
        effect_ratio_dict[effect] += 1

    chart = {
        'chart': {
            'type': 'pie'
        },
        'title': {
            'text': 'Effect Ratio'
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
    report = Report.objects.get(pk=kwargs['reportId'])

    gene_dict = {}
    for variant in report.variant_set.all():
        gene_name = variant.gene_name
        if gene_name not in gene_dict.keys():
            gene_dict[gene_name] = 0
        gene_dict[gene_name] += 1

    del gene_dict['']
    top_five_genes = sorted(gene_dict, key=gene_dict.__getitem__, reverse=True)[:5]

    chart = {
        'chart': {
            'type': 'column'
        },
        'title': {
            'text': 'Top Five Genes Occurences'
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

