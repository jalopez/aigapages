from django.http import HttpResponse, HttpResponseServerError, Http404, HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response
from aigapages.bib.models import Author, Publication

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

def process_response(publications, order_by):
    if (order_by == 'type'): 
        types = group_by_type(publications)
        return render_to_response('publications.html',
            {'list_template': 'by_type.html', 'types':  types})
    elif (order_by == 'year'):
        years = group_by_year(publications)
        return render_to_response('publications.html', 
            { 'list_template': 'by_year.html', 'type': {'years': years }}) 
    else: 
        raise Http404


def view_all(request):
    publications = Publication.objects.filter(author__institute='Facultad de Informatica')

    order_by = request.GET.get('order_by', 'year')

    return process_response(publications, order_by)

def view_author(request, author_id):
    author = get_object_or_404(Author, author_id=author_id, 
        institute='Facultad de Informatica')

    order_by = request.GET.get('order_by', 'year')

    return process_response(author.publications, order_by)


    #import ipdb; ipdb.set_trace()

# vim:set ts=4 sw=4 et:
