from django.shortcuts import HttpResponse,render
import datetime
from django import template

# Create your views here.
def index(request):
	return HttpResponse("<p>Hello Django</p>")

def today_is(request):
	now = datetime.datetime.now()
	return render(request, 'djangobin/datetime.html', {'now': now, 'template_name': 'djangobin/nav.html'})

def profile(request, username):
	return HttpResponse("<p>profile page of #{}</p>".format(username))

def book_category(request, category='sc-fi'):
	return HttpResponse("<p>Books in {} category</p>".format(category))

def extra_args(request, arg1, arg2):
	return HttpResponse("<p>arg1 : {} <br> arg2 : {}</p>".format(arg1,arg2))

def custom_response(request):
    return HttpResponse("<p>Custom response 1</p>", content_type='text/plain')

def custom_response(request):
	import json
	data = {'name' : 'yamuna', 'age' : 23 }
	return HttpResponse(json.dumps(data), content_type='application/json')

def custom_response(request):
    return HttpResponse("<h1>HTTP 404 not found</h1>", status=404)

def snippet_detail(request, snippet_slug):
	return HttpResponse('viewing snippet #{}.format(snippet_slug)')

def trending_snippets(request, language_slug=''):
    return HttpResponse("trending {} snippets".format(language_slug if language_slug else ""))
 
 
def tag_list(request, tag):
    return HttpResponse('viewing tag #{}'.format(tag))
 
 
def profile(request, username):
    return HttpResponse("<p>Profile page of #{}</p>".format(username))

