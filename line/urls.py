from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^new$', 'line.views.new_line', name='new_line'),
    url(r'^edit/(?P<line_id>[0-9]+)/$', 'line.views.edit_line', name='edit_line'),
    url(r'^delete/(?P<line_id>[0-9]+)/$', 'line.views.delete_line', name='delete_line'),
    )