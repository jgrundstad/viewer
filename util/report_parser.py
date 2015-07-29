__author__ = 'Jason Grundstad'
from django.conf import settings
import json
import os
import tablib
from viewer.models import Variant, Report


def add_goodies(atoms, headers, md_anderson_genes, eMERGE_genelist):
    for i in range(0, len(headers)):
        if not atoms[i]:
            atoms[i] = ''
        # highlight NON_SYNONYMOUS_CODING
        if headers[i] == 'effect' and atoms[i] == 'NON_SYNONYMOUS_CODING':
            atoms[i] = "<font color=green>%s</font>" % atoms[i]
        # add MDAnderson and eMERGE links to appropriate gene names
        if (headers[i] == 'gene') and (atoms[i] is not None):
            # link to genecards
            gene_card = '<a href=\"http://www.genecards.org/index.php?' + \
                'path=/Search/keyword/{g}\" target=\"_blank\" ' + \
                'title=\"GeneCards Link\">{g}</a>'.format(
                    g=atoms[i])

            # construct additional links out
            gene_str_extension = '<br><font size=-2>'

            if atoms[i].lower() in md_anderson_genes:
                gene_str_extension += '<a href=\"{link}\" target=\"_blank\"' + \
                    'title=\"MDAnderson Cancer Center\">MDAnderson</a>'.format(
                        link=md_anderson_genes[atoms[i].lower()])

            if atoms[i].upper() in eMERGE_genelist:
                gene_str_extension += ' eMERGE'

            # assemble additional links
            new_link = '{gene_card}{ext}</font>'.format(gene_card=gene_card,
                                                   ext=gene_str_extension)
            # apply changes
            atoms[i] = new_link

    return atoms


def json_from_report(filename):
    print "%s - creating json from: %s" % (os.getcwd(), filename)
    report_file = open(filename, 'r')
    header_line = report_file.readline().strip()
    splitby = ','
    if '\t' in header_line:
        splitby = '\t'
    cols = header_line.split(splitby)

    with open(settings.LINKS_OUT + 'mdanderson.json', 'r') as md_f:
        md_anderson_genes = json.loads(json.load(md_f))

    eMERGE_genelist = []
    with open(settings.LINKS_OUT + 'eMERGE_genelist.txt', 'r') as e_f:
        for line in e_f:
            gene = line.rstrip()
            if gene:
                eMERGE_genelist.append(gene)

    d = []
    for line in report_file:
        # remove '%' character to allow numerical sorting on pct columns
        #line = line.replace('%', '')
        tokens = line.rstrip('\n').split(splitby)
        if len(tokens) > 1:
            if 'INTRON' not in line and 'INTERGENIC' not in line:
                formatted_line = add_goodies(tokens, cols, md_anderson_genes, eMERGE_genelist)
                d.append(formatted_line)
    data = tablib.Dataset(*d, headers=cols)
    return data

def json_from_ajax(db_response):
    records = db_response.values()

    if len(records) == 0:
        return ''

    cols = []
    for header in records[0]:
        cols.append(header)

    vals = []
    for record in records:
        r = []
        for col in record:
            r.append(record[col])
        vals.append(r)

    return tablib.Dataset(*vals, headers=cols).html




def load_into_db(report):
    report_file = open(settings.MEDIA_ROOT + report.report_file.name, 'r')
    header_line = report_file.readline().strip()
    splitby =','
    if '\t' in header_line:
        splitby = '\t'
    cols = header_line.split(splitby)
    print "cols: {}".format(cols)

    for line in report_file:
        toks = line.rstrip('\n').split(splitby)
        if len(toks) > 1:
            variant = Variant()
            # skip over missing Int fields
            for intfield in ['pos', 'normal_ref_count', 'normal_alt_count',
                             'tumor_ref_count', 'tumor_alt_count',
                             'amino_acid_length']:
                if toks[cols.index(intfield)]:
                    setattr(variant, intfield, int(toks[cols.index(intfield)]))

            variant.report = report
            variant.chrom = toks[cols.index('chr')]
            variant.ref = toks[cols.index('ref')]
            variant.alt = toks[cols.index('alt')]
            variant.context = toks[cols.index('context')]
            variant.dbSnp_id = toks[cols.index('dbSnp_id')]
            variant.gene_name = toks[cols.index('gene')]
            variant.effect = toks[cols.index('effect')]
            variant.coding = toks[cols.index('coding')]
            variant.codon_change = toks[cols.index('codon_change')]
            variant.amino_acid_change = toks[cols.index('amino_acid_change')]
            variant.save()
