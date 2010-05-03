from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('aigapages.bib',
    (r'^$', 'views.view_all'),
    (r'^author/(?P<author_id>\d+)/$', 'views.view_author'),
    (r'^pub/(?P<pub_id>\d+)/fulltext$', 'views.download_fulltext'),
    (r'^pub/(?P<pub_id>\d+)/bibtex$', 'views.view_bibtex'),

    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^admin/', include(admin.site.urls)),
)


# vim:set ts=4 sw=4 et:
