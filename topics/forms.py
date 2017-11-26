from django import forms
from .models import Topic, Course

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['title', 'num_courses']
		labels = {'title' : 'Title', 'num_courses' : 'Number of Course'}
		
class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['date', 'time', 'room', 'course', 'value', 'status']
		labels = {'date' : 'Date', 'time' : 'Time', 'room' : 'Room', 'course' : 'Course', 'value' : 'value', 'status' : 'Status'}
		