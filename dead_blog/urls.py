from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from blog.views import post_list
from blog.views import post
from blog.views import portfolio
from blog.views import contact
from blog.views import about


urlpatterns = patterns('',
                       url(r'^$', post_list),
                       url(r'^portfolio/$', portfolio),
                       url(r'^contact/$', contact),
                       url(r'^about/$', about),
                       url(r'^([a-zA-Z0-9.-]+)/$', post),
                       url(r'^admin/', include(admin.site.urls)),
                       )
