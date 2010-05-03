from django.conf import settings
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, HttpResponseServerError, Http404, HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect
from aigapages.bib.models import Author, Publication
from os import path

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
            {'list_template': 'by_type.html', 'types':  types})
    elif (order_by == 'year'):
        years = group_by_year(publications)
        return render_to_response('publications.html', 
            { 'list_template': 'by_year.html', 'type': {'years': years }}) 
    else: 
        raise Http404


def view_all(request):
    publications = Publication.objects.filter(author__institute='Facultad de Informatica')
    return listing_response(publications, request.GET)

def view_author(request, author_id):
    author = get_object_or_404(Author, author_id=author_id, 
        institute='Facultad de Informatica')
    return listing_response(author.publications, request.GET)


def download_fulltext(request, pub_id):
    publication = get_object_or_404(Publication, pub_id = pub_id)
    attachment  = get_object_or_404(publication.attachments_set.all(), ismain=True)
    #import ipdb; ipdb.set_trace()
    if attachment.isremote: 
        return redirect(attachment.location)
    else:
        filename = path.join(settings.ATTACHMENT_DIR, attachment.location)
        response = HttpResponse(FileWrapper(file(filename)), content_type=attachment.mime)
        response['Content-Disposition'] = ('attachment; filename=%s' % attachment.name)
        return response
    
def view_bibtex(request, pub_id):
    raise Http404



# vim:set ts=4 sw=4 et:
