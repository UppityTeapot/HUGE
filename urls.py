from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('storyteller.views',
    (r'^$', 'index'),                  
    (r'^storyteller/', include('storyteller.urls')),
    (r'^admin/', include(admin.site.urls)),
)