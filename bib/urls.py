from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('aigapages.bib',
    (r'^$', 'views.view_all'),
    (r'^author/(?P<author_id>\d+)/$', 'views.view_author'),

    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^admin/', include(admin.site.urls)),
)


# vim:set ts=4 sw=4 et:
