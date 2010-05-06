from django.shortcuts import render_to_response
from django.template import RequestContext
from aigapages.authors import author_list
import re

def month_order(month):
    if month:
        return {
            '"jan"':  1,
            '"feb"':  2,
            '"mar"':  3,
            '"apr"':  4,
            '"may"':  5,
            '"jun"':  6,
            '"jul"':  7,
            '"aug"':  8,
            '"sep"':  9,
            '"oct"': 10,
            '"nov"': 11,
            '"dec"': 12,
        }[month]
    else:
        return 0


def group_by_year(publications):
    years = publications.values('year').distinct().order_by('-year')
    for year in years:
        year['publications'] = sorted(publications.filter(year=year['year']), 
                                        key=lambda pub: -month_order(pub.month))
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

def listing_response(request, publications, context={ 'title':  ''}):
    order_by = request.GET.get('order_by', 'year')
    project = request.GET.get('project', '')
    publications = publications.exclude(userfields__icontains='private={True}')

    if project:
        publications = publications.filter(userfields__icontains='project={%s}' % project)

    if (order_by == 'type'): 
        types = group_by_type(publications)
        context.update({'list_template': 'by_type.html', 'types':  types, 
                'authors': author_list})
        return render_to_response('publications.html', context, 
                    context_instance=RequestContext(request))
            
    elif (order_by == 'year'):
        years = group_by_year(publications)
        context.update({ 'list_template': 'by_year.html', 'type': {'years': years }, 
                'authors': author_list}) 
        return render_to_response('publications.html', context,
                    context_instance=RequestContext(request))
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
