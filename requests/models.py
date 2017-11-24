from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
	#A request for covering hours
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	time = models.CharField(max_length=200)
	room = models.CharField(max_length=200)
	course = models.CharField(max_length=200)
	value = models.CharField(max_length=200)
	#comment = models. #will add in intial comment later
	date_posted = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		#return a string representation of the request
		return self.title
	
	
class Comment(models.Model):
	#a comment on a request
	request = models.ForeignKey(Request)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'comments'
		
	def __str__(self):
		#return a string representation of the comment
		return self.text