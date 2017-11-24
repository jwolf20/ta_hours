from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Request, Comment
from .forms import RequestForm

def index(request):
	#the home page for ta_hours
	return render(request, 'requests/index.html')
	
def requests(request):
	#show all requests.
	requests = Request.objects.order_by('date_posted')
	context = {'requests': requests}
	return render(request, 'requests/requests.html', context)
	
def new_request(request):
	#post a new request
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form  = RequestForm()
		
	else:
		#POST data submitted; process data.
		form = RequestForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('requests:requests'))
			
	context = {'form': form}
	return render(request, 'requests/new_request.html', context)
	
def comments(request, request_id):
	#show a single reuest and all its comments
	r = Request.objects.get(id=request_id)
	comments = r.comment_set.order_by('-date_added')
	context = {'request':r, 'comments': comments}
	return render(request, 'requests/comments.html', context)
	