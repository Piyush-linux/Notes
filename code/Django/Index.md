__Install__ => `pip install Django`
__Version__ => `python -m django --version`
_Help_ => `django-admin`
_Project_=>`django-admin startproject`
    - Create require folder
    - manage.py : command line utility
    - init.py : python package
    - url.py : url declaration
    - wsgl.py : webserver gateway interface
_Run_:python manage.py runserver
    - open port link
_views_:
_urls_:
    - ulf.py : from . import file
    - url : `path('about',views.about,name='about')`||(url/,file.function,name='name') : end point
    - path('',views.index,name='base'), => require base url
    - link : port/function_name
```py
f1:
from . import master
url{
    path('',views.index,name='base'),
    path('home',views.home,name='home'),
}
f2:from django .http import HttpResponse
    def index(request):
        return HttpResponse("<h1>Hello  Piyush</h1>")
    def home(request):
        return HttpResponse("<a href='/'>Home</a>")
```
> Exercise :: Execute txt file in site

+ __PipeLine__
    - path('',views.index,name='base')
    - path('a',views.a,name='a')
    - path('b',views.b,name='b')
+ __Template__
    - setting.py : TEMPLATE{DIR=['folder']}
    - views.py : 
```py
from django.shortcuts import render 

def index(request):
    var={'name':"piyush"}
    return render(request,'index.html',var)

file.html: My name is {{name}} ==>  My name is piyush
```
    - make file.html in manage.py section
```python
def a(request):
    name=(request.GET.get('usrName','default'))#r.G.g('name of input','default')
    print(name)
    male=(request.GET.get('male','on'))#(checkbox,on/off)>to get info 
    print(male)
    var={'name':name.title(),'male':male}
    return render(request,'submit.html',var) 
```