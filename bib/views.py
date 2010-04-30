from django.http import HttpResponse, HttpResponseServerError, Http404, HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response
from aigapages.bib.models import Author, Publication

def group_by_year(publications):
    years = publications.values('year').distinct().order_by('-year')
    for year in years:
        year['publications'] = publications.filter(year=year['year'])
    return years


def view_all(request):
    publications = Publication.objects.filter(author__institute='Facultad de Informatica')
    years = group_by_year(publications)

    return render_to_response('publications.html', 
        { 'list_template': 'by_year.html', 'years': years }) 


def view_author(request, author_id):
    author = get_object_or_404(Author, author_id=author_id, 
        institute='Facultad de Informatica')
    years = group_by_year(author.publications)

    return render_to_response('publications.html', 
        { 'list_template': 'by_year.html', 'years': years }) 

    #import ipdb; ipdb.set_trace()

# vim:set ts=4 sw=4 et:
