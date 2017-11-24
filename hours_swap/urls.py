#Defines URL patterns for hours_swap

from django.conf.urls import url

from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.index, name='index'),
    
    #Show all requests
    url(r'^cover_requests/$', views.cover_requests, name='cover_requests'),
    
    #Detail page for a single topic
    #url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    
    #page for adding a new cover_request
    url(r'^new_cover_request/$', views.new_cover_request, name='new_cover_request'),
    
    #page for adding a new cover_reply
    url(r'^new_cover_reply/(?P<cover_request_id>\d+)/$', views.new_cover_reply, name='new_cover_reply'),
    
    #page for editing a cover_request
    url(r'^edit_cover_request/(?P<cover_request_id>\d+)/$', views.edit_cover_request, name='edit_cover_request'),

    #page for editing an cover_reply
    url(r'^edit_cover_reply/(?P<cover_reply_id>\d+)/$', views.edit_cover_reply, name='edit_cover_reply'),
    
]


