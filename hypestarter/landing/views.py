from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Featured

def index(request):
	"""Index Page

	Landing page for the website.

	"""
	# Collect data for index page
	try:
		featured = Featured.objects.latest()
	except Featured.DoesNotExist:
		featured = None
	return render_to_response(
		'landing/index.html',
		{
			'featured': featured,
		},
		context_instance=RequestContext(request)
	)

def about(request):
	"""About Page

	Displays information about the project and the team behind it.

	"""
	# Collect data for index page
	return render_to_response('landing/index.html', context_instance=RequestContext(request))

def code(request):
	"""Index Page

	Landing page for the website.

	"""
	# Collect data for index page
	return render_to_response('landing/index.html', context_instance=RequestContext(request))