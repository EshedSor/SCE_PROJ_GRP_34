from django.shortcuts import render
from django.shortcuts import HttpResponse
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
   return render(request,"SCE_Proj/template/LogIn.html")
"""   Eshed Sorosky 
      28/Nov/21
      return LogIn """
def homepage(request):
   return render(request, "SCE_Proj/template/homepage.html")