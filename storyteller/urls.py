from django.conf.urls.defaults import *

urlpatterns = patterns('storyteller.views',
    (r'^$', 'index'),
    (r'^place/$', 'placeindex'),                   
    (r'^place/(?P<place_id>\d+)/$', 'place'),
)
