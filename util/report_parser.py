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
            atoms[i] = "<span style=\"color:green\">%s</span>" % atoms[i]
        # add MDAnderson and eMERGE links to appropriate gene names
        if (headers[i] == 'gene') and (atoms[i] is not None):
            # link to genecards
            gene_card = ('<a href=\"http://www.genecards.org/index.php?' +
                         'path=/Search/keyword/{g}\" target=\"_blank\" ' +
                         'title=\"GeneCards Link\">{g}</a>').format(g=atoms[i])

            # construct additional links out
            gene_str_extension = '<br/><span style=\"font-size:x-small\">'

            if atoms[i].lower() in md_anderson_genes:
                gene_str_extension += '<a href=\"{link}\" target=\"_blank\"' + \
                    'title=\"MDAnderson Cancer Center\">MDAnderson</a>'.format(
                        link=md_anderson_genes[atoms[i].lower()])

            if atoms[i].upper() in eMERGE_genelist:
                gene_str_extension += ' eMERGE'

            # assemble additional links
            new_link = '{gene_card}{ext}</span>'.format(gene_card=gene_card,
                                                   ext=gene_str_extension)
            # apply changes
            atoms[i] = new_link

    return atoms

def get_mdanderson_genes():
    with open(settings.LINKS_OUT + 'mdanderson.json', 'r') as md_f:
        return json.loads(json.load(md_f))

def get_eMERGE_genelist():
    eMERGE_genelist = []
    with open(settings.LINKS_OUT + 'eMERGE_genelist.txt', 'r') as e_f:
        for line in e_f:
            gene = line.rstrip()
            if gene:
                eMERGE_genelist.append(gene)
    return eMERGE_genelist

def json_from_report(filename):
    print "%s - creating json from: %s" % (os.getcwd(), filename)
    report_file = open(filename, 'r')
    header_line = report_file.readline().strip()
    splitby = ','
    if '\t' in header_line:
        splitby = '\t'
    cols = header_line.split(splitby)

    md_anderson_genes = get_mdanderson_genes()
    eMERGE_genelist = get_eMERGE_genelist()

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
    # Make sure query returned some data
    # If not, report back empty
    if len(db_response) == 0:
        return ''

    md_anderson_genes = get_mdanderson_genes()
    eMERGE_genelist = get_eMERGE_genelist()

    # Pull headers, sort into alphabetical order
    # This is so it's in the same order returned
    # by Variant._meta.get_all_field_names()
    headers = []
    for header in db_response.values()[0]:
        headers.append(header)
    headers.sort()

    # Grab and store pre-rearranged indexes of relevant headers
    col_order = [headers.index('chrom'), headers.index('pos'), headers.index('gene_name'), headers.index('ref'),
                  headers.index('alt'), headers.index('normal_ref_count'), headers.index('normal_alt_count'),
                  headers.index('tumor_ref_count'), headers.index('tumor_alt_count')]

    # Rearrage headers
    new_headers = []
    for i in col_order:
        new_headers.append(headers[i])
        headers[i] = None
    map(lambda x: new_headers.append(x) if x else False, headers)
    headers = new_headers

    # Append extra headers to front
    headers.insert(0, 'BnIDs')
    headers.insert(0, 'sample')
    headers.insert(0, 'study')

    # Temporary to make search and view report agree on the header for the gene name
    # TODO
    headers[headers.index('gene_name')] = 'gene'

    # Parse list of variant records
    variant_records = []
    for variant in db_response:
        # Get all field names, delete report object
        field_names = Variant._meta.get_all_field_names()
        del field_names[field_names.index('report')]

        # Pull relevent fields from variant object
        record = []
        for key in field_names:
            if key in variant.__dict__:
                record.append(variant.__dict__[key])

        # Replace all None with empty string
        record = ['' if elem is None else elem for elem in record]

        # Sort the records into desired order
        new_record = []
        for i in col_order:
            new_record.append(record[i])
            record[i] = None
        map(lambda x: new_record.append(x) if x is not None else False, record)
        record = new_record

        # Append extra data to front
        bnids, samples = [], set()
        for bnid in variant.report.bnids.all():
            bnids.append(bnid.bnid)
            samples.add(bnid.sample.name)
        bnids = map(str, bnids)
        samples = map(str, samples)
        study = variant.report.study.name
        record = [study, str(samples), str(bnids)] + record

        # This doesn't allow through records that have INTRON or INTERGENIC
        # Is that what we want?
        # TODO
        if len(record) > 1:
            if 'INTRON' not in record and 'INTERGENIC' not in record:
                formatted_record = add_goodies(record, headers, md_anderson_genes, eMERGE_genelist)
                # Append this record to list of all records
                variant_records.append(formatted_record)

    # Return as an html table
    return tablib.Dataset(*variant_records, headers=headers).html


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
