#Created by me - Piyush
from django .http import HttpResponse
from django.shortcuts import render

def index(request):
	var={'name':"piyush"}
	return render(request,'index.html',var)

def home(request):
	return HttpResponse("Home Page")

def pipe(request):
	return HttpResponse("Pipe <br> <a href='/'>Home</a> <br> <a href='/a'>First</a>")

def a(request):
	name=(request.GET.get('usrName','default'))#r.G.g('name of that tag','default')
	print(name)
	male=(request.GET.get('male','on'))#(checkbox,on/off)>to get info 
	print(male)
	var={'name':name.title(),'male':male}
	return render(request,'submit.html',var)

def b(request):
	return HttpResponse("Second")

