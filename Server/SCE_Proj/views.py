from django import http
from django.shortcuts import render,redirect, render
from django.shortcuts import HttpResponse
from django.template import RequestContext
from .forms import loginForm,RegisterForm,settings_info
from django.contrib import messages
from SCE_Proj.models import bloguser
import datetime
from django.core.mail import send_mail

COOKIE_TIMEOUT = 600
#--------------------------------------------
""" Eshed Sorosky 
      7/DEC/21
      return regsiter page  """
def get_bloguser_ob(request):
   """the function returns a blogspot user from the database using cookies"""
   email = request.COOKIES.get('email')
   dbuser = bloguser.objects.get(email = email)
   return dbuser
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
def verify_cookie(request):
   """returns true/false if cookie is legit"""
   if 'email' in request.COOKIES and 'last_connection' in request.COOKIES:
      last_connection = request.COOKIES.get('last_connection')
      last_connection_time = datetime.datetime.strptime(last_connection[:-7],"%Y-%m-%d %H:%M:%S")
      if(datetime.datetime.now() - last_connection_time).seconds < COOKIE_TIMEOUT:
         return True
   return False
#--------------------------------------------
"""   Eshed Sorosky 
      28/Nov/21
      return Landingpage """
def LandingPage(request):
   if verify_cookie(request):
      #return HttpResponse(str(verify_cookie(request)))
      return redirect('homepage')
   return render(request,"SCE_Proj/template/landingpage.html")
#--------------------------------------------
"""   Eshed Sorosky 
      28/Nov/21
      return login """
def login(request):
   #added by eshed in 29/NOV/21
   #if data was sent to the server
   if(request.method == "POST"):
      #filling the form with the relevant data
      this_form = loginForm(request.POST)
      #if the credentials are correct
      if this_form.is_valid():
         #adding to the response the html page to represent
         response = redirect('homepage')
         #setting the cookies since the form was valid
         response.set_cookie('last_connection', datetime.datetime.now())
         response.set_cookie('email',this_form.cleaned_data.get('email'))
      #if the form wasnt valid then refresh the login form and edit the response accodingly
      else:
         this_form = loginForm()
         response = render(request,'SCE_Proj/template/login.html')
      return response
      #for cookie support
   #if this is a GET response that means we didnt submit any form
   elif(request.method == 'GET'):
      if verify_cookie(request):
         return redirect('homepage')
      else:
         return render(request, "SCE_Proj/template/login.html")
#--------------------------------------------
"""   Eshed Sorosky 
      28/Nov/21
      return login """
def homepage(request):
   path = "SCE_Proj/template/homepage-XXX.html"
   if verify_cookie(request):
      dbuser = get_bloguser_ob(request)
      dbrole = dbuser.role
      path = path.replace("XXX",dbrole)
      response = render(request,path,{"fullsname":"{0} {1}".format(dbuser.name,dbuser.surname),
                                            "nickname":dbuser.nickname,
                                            "role":dbrole})
      
      return response
   else:
      path = path.replace("XXX","guest")
   return render(request,path)

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
         return redirect("http://explorair.link/login")
      else:
         form = RegisterForm()
         response = render(request,'SCE_Proj/template/register.html')
   elif(request.method == 'GET'):
      if verify_cookie(request):
         return redirect('homepage')
   return render(request,'SCE_Proj/template/register.html')
#--------------------------------------------
"""   Eshed Sorosky 
      25/DEC/21
      return about page page  """
def about_page(request):
   """the function returns the about page"""
   return render(request,'SCE_Proj/template/about_page.html')
#--------------------------------------------
"""   Eshed Sorosky 
      25/DEC/21
      return about setting page  """
def settings_page(request):
   """the function returns the about page"""
   if request.method == 'POST':
      #if 'update_info' in request.POST:
      form = settings_info(request.POST)
      if(form.is_valid):
         dbuser = get_bloguser_ob(request)
         if form.cleaned_data.get('name')!=None:               
            dbuser.name = form.cleaned_data.get('name')
         if form.cleaned_data.get('surname'):
            dbuser.surname = form.cleaned_data.get('surname')
         if form.cleaned_data.get('nickname'):
            dbuser.nickname = form.cleaned_data.get('nickname')
            return HttpResponse(form.cleaned_data.get('nickname'))
         if form.cleaned_data.get('bio'):
            dbuser.bio = form.cleaned_data.get('bio')
         dbuser.save()
   if request.method == 'GET':
      if verify_cookie(request):
         dbuser = get_bloguser_ob(request)
         return render(request,'SCE_Proj/template/setting_page.html',
         {
            'fullname':"{0} {1}".format(dbuser.name,dbuser.surname),
            'firstname':dbuser.name,
            'lastname':dbuser.surname,
            'nickname':dbuser.nickname,
            'bio':dbuser.bio
         })
      return redirect('login')