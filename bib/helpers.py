from django.shortcuts import render_to_response
from aigapages.authors import author_list
import re

def group_by_year(publications):
    years = publications.values('year').distinct().order_by('-year')
    for year in years:
        year['publications'] = publications.filter(year=year['year'])
    return years

def group_by_type(publications):
    all_types = map(lambda t: t['pub_type'],
         publications.values('pub_type').distinct().order_by('pub_type'))

    types = []
    for type in ('Article', 'Inproceedings', 'Book', 'Proceedings', 'Inbook',
        'Incollection', 'Phdthesis', 'Mastersthesis', 'Booklet', 'Manual',
        'Techreport', 'Misc', 'Unpublished'):

        if type in all_types: 
            all_pubs = publications.filter(pub_type=type)
            types += [{
                'years': group_by_year(all_pubs),
                'pub_type': type,
            }]

    return types

def listing_response(publications, params, context={}):
    order_by = params.get('order_by', 'year')
    project = params.get('project', '')

    if project:
        publications = publications.filter(userfields__icontains='project={%s}' % project)

    if (order_by == 'type'): 
        types = group_by_type(publications)
        context.update({'list_template': 'by_type.html', 'types':  types, 
                'authors': author_list})
        return render_to_response('publications.html', context)
            
    elif (order_by == 'year'):
        years = group_by_year(publications)
        context.update({ 'list_template': 'by_year.html', 'type': {'years': years }, 
                'authors': author_list}) 
        return render_to_response('publications.html', context)
    else: 
        raise Http404


def print_authors(author_list): 
    return ' and '.join(map(lambda e: e.cleanname, author_list))


def parse_userfields(userfields):
    parsed_userfields = []
    
    for match in re.finditer(r'(?P<key>\w+)\s*=\s*{(?P<value>[^}]*)},', userfields):
        parsed_userfields += [(match.group('key'), match.group('value'))]
    return parsed_userfields


# vim:set ts=4 sw=4 et:
