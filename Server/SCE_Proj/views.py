from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.template import RequestContext
from .forms import LoginForm,RegisterForm
from SCE_Proj.models import bloguser
# Create your views here.
from django.shortcuts import render

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
         return render(request, 'SCE_Proj/template/homepage.html')
      else:
         this_form = LoginForm()
         return HttpResponse("<h1>bad input</h1>")

   return render(request, 'SCE_Proj/template/logIn.html')

   #response.set_cookie('last_connection', datetime.datetime.now())
   #response.set_cookie('username', datetime.datetime.now())
	
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
      if form.is_valid():
         form.save()
      return render(request,"SCE_Proj/template/homepage.html")
   else:
      form = RegisterForm()
   return render(request,"SCE_Proj/template/register.html")


