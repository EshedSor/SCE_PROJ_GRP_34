from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from django.shortcuts import render

def hello(request):
   return render(request, "SCE_Proj/template/hello.html", {})
"""def hello(request):
   text = <h1>welcome to my app !</h1>
   return HttpResponse(text)"""