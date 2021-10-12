from typing import ContextManager
from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    context={
        'variable':'this is sent and it will be written in web up to this dot',
        'varaible2':"this bold is also sent through variable in django"
    }
    return render(request,"home.html",context)
    # return HttpResponse('This is an Homepage')

def  about(request):
    return render(request,"about.html",)

def services(request):
    return render(request,"services.html",)

def login(request):
    return render(request,"login.html")





