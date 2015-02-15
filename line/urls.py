from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^(?P<item_pk>\d+)/$', 'line.views.detail_view', name='detail_view'),
    url(r'^newline$', 'line.views.new_line', name='new_line'),
    url(r'^newcategory$', 'line.views.new_category', name='new_category'),
    url(r'^edit/(?P<line_id>[0-9]+)/$', 'line.views.edit_line', name='edit_line'),
    url(r'^delete/(?P<line_id>[0-9]+)/$', 'line.views.delete_line', name='delete_line'),
    url(r'^new_comment/(?P<item_id>[0-9]+)/$', 'line.views.new_comment', name='new_comment'),
    url(r'^edit_comment/(?P<comment_id>[0-9]+)/$', 'line.views.edit_comment', name='edit_comment'),
    )