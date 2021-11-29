"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from SCE_Proj import views
#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
import SCE_Proj

urlpatterns = [
    # admin console
    path('admin/', admin.site.urls),
    # hello page
    path('hello/', SCE_Proj.views.hello, name = 'hello'),
    # default page
    path('', SCE_Proj.views.default_redirect, name = "default_redirect"),
    # landingpage
    path('landingpage/',SCE_Proj.views.LandingPage, name = "landingpage"),
    #login page
    path('LogIn/',SCE_Proj.views.LogIn,name = "LogIn"),
    #homepage
    path('homepage/',SCE_Proj.views.homepage,name = 'homepage'),
    #ajax
   # url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls'))
]
#urlpatterns += staticfiles_urlpatterns()