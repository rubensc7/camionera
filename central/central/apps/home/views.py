# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def Inicio(request):
	return render_to_response('home/base.html')