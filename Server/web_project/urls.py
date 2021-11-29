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
import SCE_Proj

urlpatterns = [
    # admin console
    path('admin/', admin.site.urls),
    # hello page
    path('hello/', SCE_Proj.views.hello, name = 'hello'),
    # default page
    path('', SCE_Proj.views.hello, name = 'hello'),
    # landingpage
    path('landingpage/',SCE_Proj.views.LandingPage, name = "landingpage"),
]
