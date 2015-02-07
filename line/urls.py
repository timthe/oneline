from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^new$', 'line.views.new_line', name='new_line'),
    )