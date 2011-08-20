from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'huge_placeholder.views.home', name='home'),
    # url(r'^huge_placeholder/', include('huge_placeholder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^place/$', 'storyteller.views.index'),
    (r'^place/(?P<place_id>\d+)/$', 'storyteller.views.place'),
    url(r'^admin/', include(admin.site.urls)),
)
