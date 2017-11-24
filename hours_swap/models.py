from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cover_Request(models.Model):
	#A request for office hours to be covered
	request_title = models.CharField(max_length=200)
	request_course = models.CharField(max_length=200)
	request_room = models.CharField(max_length=200)
	request_time = models.CharField(max_length=200)
	request_date = models.CharField(max_length=200)
	request_value = models.CharField(max_length=200)
	request_notes = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)
    
	def __str__(self):
		#return a string representation of the model.
		return self.request_title
	
class Cover_Reply(models.Model):
	#reply to a request
	cover_request = models.ForeignKey(Cover_Request)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)
	
	class Meta:
		verbose_name_plural = 'replies'
	
	def __str__(self):
		#return a string represenation of the model.
		return self.text[:50] + '...'