from django import http
from django.shortcuts import render,redirect, render
from django.shortcuts import HttpResponse
from django.template import RequestContext
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from SCE_Proj.models import bloguser
import datetime
from django.core.mail import send_mail
#--------------------------------------------
"""   Eshed Sorosky 
      6/DEC/21
      sending welcome email """
def welcome_mail(request,recipient):
      send_mail(
         'Welcome to our blog',
         'Hey ' +recipient['name'] +" "+recipient['surname'] +" we welcome you to our blog",
         'system@explorair.link',
         [recipient['email']],
         fail_silently= False,
      )
#--------------------------------------------
"""   Eshed Sorosky 
      6/DEC/21
      checking cookies """
def check_cookies(request, url, path):
   """the function receives a request http object, url for redirect and path for html and checks
      if the cookies are still legit and redirect you or renders a relevant page based on the parameters passed"""
   #checking if there are cookies
   if 'email' in request.COOKIES and 'last_connection' in request.COOKIES:
      email = request.COOKIES.get('email')
      #checking if cookie exist
      last_connection = request.COOKIES.get('last_connection')
      last_connection_time = datetime.datetime.strptime(last_connection[:-7],"%Y-%m-%d %H:%M:%S")
      #cookie session is 30 seconds
      if(datetime.datetime.now() - last_connection_time).seconds < 30:
         response = redirect(url)
      #if the cookies are past due then return to the relevant page
      else:
         response = render(request,path)
   #if there arent cookies just sets the response to the relevant page page
   else:
      response = render(request,path)
   return response
#--------------------------------------------
"""   Eshed Sorosky 
      28/Nov/21
      return Landingpage """
def LandingPage(request):
   response = check_cookies(request,"http://explorair.link/homepage","SCE_Proj/template/landingpage.html")
   return response
#--------------------------------------------
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
      response = check_cookies(request,"http://explorair.link/homepage","SCE_Proj/template/logIn.html")
   return response
#--------------------------------------------
"""   Eshed Sorosky 
      28/Nov/21
      return LogIn """
def homepage(request):
   return render(request, "SCE_Proj/template/homepage.html")
#--------------------------------------------
"""   Eshed Sorosky 
      29/Nov/21
      redirect from default dns  """
def default_redirect(request):
   return LandingPage(request)
"""   Eshed Sorosky 
      29/Nov/21
      return regsiter page  """
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
         """
         #sending welcome email, building the value dict
         welcome_mail(
            request,
               {
                  "name":form.cleaned_data.get('name'),
                  "surname":form.cleaned_data.get('surname'),
                  "email":form.cleaned_data.get('email')
               }
            )
         """
         return redirect("http://explorair.link/logIn")
      else:
         form = RegisterForm()
         response = render(request,'SCE_Proj/template/register.html')
   elif(request.method == 'GET'):
      #checking if there are cookies
      response = check_cookies(request,"http://explorair.link/homepage","SCE_Proj/template/register.html")
   return response
#--------------------------------------------




