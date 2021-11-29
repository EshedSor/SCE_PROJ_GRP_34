from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.template import RequestContext
from .forms import Login
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
   username = "not logged in"
   #if data was sent to the server
   if(request.method == "GET"):
      return render(request,"SCE_Proj/template/logIn.html")
   elif(request.method == "POST"):
      #filling the form with the relevant data
      this_form = Login(request.POST)
   #if the credentials are correct
   if this_form.is_valid():
      username = this_form.cleaned_data['username']
      return render(request, 'SCE_Proj/template/homepage.html', {"username" : username})
   else:
      this_form = Login()

   return render(request, 'SCE_Proj/template/logIn.html', {"username" : username})

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
   return render(request,"SCE_Proj/template/register.html")
