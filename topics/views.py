from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Comment, Course
from .forms import TopicForm, CourseForm

def index(request):
	#the home page for ta_hours
	return render(request, 'topics/index.html')
	
def topics(request):
	#show all topics.
	topics = Topic.objects.order_by('-date_posted')
	context = {'topics': topics}
	return render(request, 'topics/topics.html', context)

@login_required
def new_topic(request):
	#post a new topic
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form  = TopicForm()
		
	else:
		#POST data submitted; process data.
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('topics:topics'))
			
	context = {'form': form}
	return render(request, 'topics/new_topic.html', context)

@login_required
def new_course(request, topic_id):
	#add a new course
	if request.method != 'POST':
		#no data submitted; create a blank form.
		form = CourseForm()
	
	else:
		#POST data submitted; process data.
		form = RequestForm(request.POST)
		if form.is_valid():
			new_course = form.save(commit=False)
			new_course.topic = Topic.objects.get(id=topic_id)
			new_course.save()
			return HttpResponseRedirect(reverse('topics:topics'))
			
	context = {'form': form}
	return render(request, 'topics/new_course.html', context)
	
@login_required	
def comments(request, topic_id):
	#show a single reuest and all its comments
	t = Topic.objects.get(id=topic_id)
	courses = t.course_set
	comments = t.comment_set.order_by('-date_added')
	context = {'topic': t, 'comments': comments, 'courses' : courses}
	return render(request, 'topics/comments.html', context)
	