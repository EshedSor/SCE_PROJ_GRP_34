from django import http
from django.shortcuts import render,redirect, render
from django.shortcuts import HttpResponse
from django.template import RequestContext
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from SCE_Proj.models import bloguser
import datetime

def hello(request):
   return render(request, "SCE_Proj/template/hello.html", {})

"""   Eshed Sorosky 
      28/Nov/21
      return Landingpage """
def LandingPage(request):
   return render(request,"SCE_Proj/template/landingpage.html")

"""   Eshed Sorosky 
      28/Nov/21
      return LogIn """
def LogIn(request):
   #added by eshed in 29/NOV/21
   #if data was sent to the server
   if(request.method == "POST"):
      #filling the form with the relevant data
   
      this_form = LoginForm(request.POST)
      #if the credentials are correct
      if this_form.is_valid():
         response = render(request,'SCE_Proj/template/homepage.html')
         response.set_cookie('last_connection', datetime.datetime.now())
         response.set_cookie('email',datetime.datetime.now())
      else:
         this_form = LoginForm()
         response = render(request,'SCE_Proj/template/logIn.html')
      #for cookie support
   elif(request.method == 'GET'):
      if 'email' in request.COOKIES and 'last_connection' in request.COOKIES:
         email = request.COOKIES.get('email')
         #checking if cookie exist
         last_connection = request.COOKIES.get('last_connection')
         last_connection_time = datetime.datetime.strptime(last_connection[:-7],"%Y-%m-%d %H:%M:%S")
         if(datetime.datetime.now() - last_connection_time).seconds < 30:
            response = render(request,'SCE_Proj/template/homepage.html')
         else:
           response = render(request,'SCE_Proj/template/logIn.html')
      else:
         response = render(request,'SCE_Proj/template/logIn.html')
   return response

"""   Eshed Sorosky 
      28/Nov/21
      return LogIn """
def homepage(request):
   return render(request, "SCE_Proj/template/homepage.html")

"""   Eshed Sorosky 
      29/Nov/21
      redirect from default dns  """
def default_redirect(request):
   return redirect(LandingPage)
"""   Eshed Sorosky 
      29/Nov/21
      return regsitet page  """
def register(request):
   if request.method == "POST":
      form = RegisterForm(request.POST)
      #return HttpResponse(form.cleaned_data.get('email'))
      if form.is_valid():
         dbuser = bloguser(
            name = form.cleaned_data.get('name'),
            surname = form.cleaned_data.get('surname'),
            password = form.cleaned_data.get('password'),
            email = form.cleaned_data.get('email')
         )
         dbuser.save()
         return render(request,"SCE_Proj/template/homepage.html")
   else:
      form = RegisterForm()
   return render(request,"SCE_Proj/template/register.html")


