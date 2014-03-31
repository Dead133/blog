from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import home
from views import hello
from views import current_datetime
from views import hours_ahead


urlpatterns = patterns('',
                       url(r'^$', home),
                       url(r'^hello/$', hello),
                       url(r'^current_datetime/$', current_datetime),
                       url(r'^time/plus/(\d{1,2})/$', hours_ahead),
                       url(r'^admin/', include(admin.site.urls)),
                       )
