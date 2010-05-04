from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^bib/', include('aigapages.bib.urls')),
    (r'^CACHE/(?P<path>.*)$','django.views.static.serve', {'document_root':'/home/jlopez/Documentos/workspace/aigapages/CACHE/'}),

    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^admin/', include(admin.site.urls)),
)

# vim:set ts=4 sw=4 et:
