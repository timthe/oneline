from django.conf.urls import patterns, include, url
from django.contrib import admin
from oneline.settings import MEDIA_ROOT

urlpatterns = patterns('',
    url(r'^$', 'line.views.home', name='home'),
    url(r'^line/', include('line.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', 'accounts.views.register', name='register'),
    url(r'^profile/$', 'accounts.views.profile', name='profile'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
