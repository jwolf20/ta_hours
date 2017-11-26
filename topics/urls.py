#Defines URL patterns for requests

from django.conf.urls import url

from . import views

urlpatterns = [
	#Home page
	url(r'^$', views.index, name='index'),
	
	#Show all topics.
	url(r'^topics/$', views.topics, name='topics'),
	
	#page for adding a new topic
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	
	#page for adding a new course
	url(r'^new_course/$', views.new_course, name='new_course'),
	
	#comment page for a single request
	url(r'^topics/(?P<topic_id>\d+)/$', views.comments, name='comments'),
]