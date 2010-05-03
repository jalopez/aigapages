from django.shortcuts import render_to_response
from aigapages.authors import author_list
import re

def group_by_year(publications):
    years = publications.values('year').distinct().order_by('-year')
    for year in years:
        year['publications'] = publications.filter(year=year['year'])
    return years

def group_by_type(publications):
    types = publications.values('pub_type').distinct().order_by('pub_type')
    for t in types:
        all_pubs = publications.filter(pub_type=t['pub_type'])
        t['years'] = group_by_year(all_pubs)
    return types

def listing_response(publications, params):
    order_by = params.get('order_by', 'year')
    project = params.get('project', '')

    if project:
        publications = publications.filter(userfields__icontains='project={%s}' % project)

    if (order_by == 'type'): 
        types = group_by_type(publications)
        return render_to_response('publications.html',
            {'list_template': 'by_type.html', 'types':  types, 'authors': author_list})
    elif (order_by == 'year'):
        years = group_by_year(publications)
        return render_to_response('publications.html', 
            { 'list_template': 'by_year.html', 'type': {'years': years }, 
		'authors': author_list}) 
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
