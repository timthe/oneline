from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'line.views.home', name='home'),
    url(r'^line/', include('line.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', 'line.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
)
