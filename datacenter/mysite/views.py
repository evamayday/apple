from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
	myname = "Eva"
	return render(request,'index.html',locals())
