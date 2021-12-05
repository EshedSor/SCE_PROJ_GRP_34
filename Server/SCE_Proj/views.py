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
   #checking if there are cookies
   if 'email' in request.COOKIES and 'last_connection' in request.COOKIES:
      email = request.COOKIES.get('email')
      #checking if cookie exist
      last_connection = request.COOKIES.get('last_connection')
      last_connection_time = datetime.datetime.strptime(last_connection[:-7],"%Y-%m-%d %H:%M:%S")
      #cookie session is 30 seconds
      if(datetime.datetime.now() - last_connection_time).seconds < 30:
         response = redirect('http://explorair.link/homepage')
      #if the cookies are past due then return to the login page
      else:
        response = render(request,'SCE_Proj/template/landingpage.html')
   #if there arent cookies just sets the response to the login page
   else:
      response = render(request,'SSCE_Proj/template/landingpage.html')
   return response

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
         #adding to the response the html page to represent
         response = redirect('http://explorair.link/homepage')
         #setting the cookies since the form was valid
         response.set_cookie('last_connection', datetime.datetime.now())
         response.set_cookie('email',datetime.datetime.now())
      #if the form wasnt valid then refresh the login form and edit the response accodingly
      else:
         this_form = LoginForm()
         response = render(request,'SCE_Proj/template/logIn.html')
      #for cookie support
   #if this is a GET response that means we didnt submit any form
   elif(request.method == 'GET'):
      #checking if there are cookies
      if 'email' in request.COOKIES and 'last_connection' in request.COOKIES:
         email = request.COOKIES.get('email')
         #checking if cookie exist
         last_connection = request.COOKIES.get('last_connection')
         last_connection_time = datetime.datetime.strptime(last_connection[:-7],"%Y-%m-%d %H:%M:%S")
         #cookie session is 30 seconds
         if(datetime.datetime.now() - last_connection_time).seconds < 30:
            response = redirect('http://explorair.link/homepage')
         #if the cookies are past due then return to the login page
         else:
           response = render(request,'SCE_Proj/template/logIn.html')
      #if there arent cookies just sets the response to the login page
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
   return LandingPage(request)
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
         return redirect("http://explorair.link/homepage")
      else:
         form = RegisterForm()
         response = render(request,'SCE_Proj/template/register.html')
   elif(request.method == 'GET'):
      #checking if there are cookies
      if 'email' in request.COOKIES and 'last_connection' in request.COOKIES:
         email = request.COOKIES.get('email')
         #checking if cookie exist
         last_connection = request.COOKIES.get('last_connection')
         last_connection_time = datetime.datetime.strptime(last_connection[:-7],"%Y-%m-%d %H:%M:%S")
         #cookie session is 30 seconds
         if(datetime.datetime.now() - last_connection_time).seconds < 30:
            response = redirect('http://explorair.link/homepage')
         #if the cookies are past due then return to the login page
         else:
           response = render(request,'SCE_Proj/template/register.html')
      #if there arent cookies just sets the response to the login page
      else:
         response = render(request,'SCE_Proj/template/register.html')
   return response


