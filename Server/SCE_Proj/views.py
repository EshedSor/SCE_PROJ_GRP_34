from django import http
from django.http.request import HttpRequest
from django.shortcuts import render,redirect, render
from django.shortcuts import HttpResponse
from django.template import RequestContext
from .forms import loginForm,RegisterForm,settings_info,new_post,search_form
from django.contrib import messages
from SCE_Proj.models import bloguser,Post
import datetime
from django.core.mail import send_mail

COOKIE_TIMEOUT = 600
#
#--------------------------------------------
""" Eshed Sorosky 
      7/DEC/21
      return search filter  """
def search_feature(search_tags,x):
   search_tags = search_tags.split(" ")
   check = False
   for i in search_tags:
      if i in x.tags:
         check = True
   return check

#--------------------------------------------
""" Eshed Sorosky 
      7/DEC/21
      return list of posts page  """
def get_post_list(request,page,filter_tag,search_tags):
   """amount - how many posts returned
      filter - what filter to apply"""
   if filter_tag == "search":
      post_list = Post.objects.order_by('-created')
      post_list = list(filter(search_feature,post_list))
      post_list = post_list[page*5:(page+1)*5]
   elif  filter_tag == "homepage":
      post_list = Post.objects.order_by('-created')[:3]
   return post_list
#--------------------------------------------
""" Eshed Sorosky 
      7/DEC/21
      return list of posts page  """
def create_post_dict(request,post_list):
   dictionary = {}
   for i in range(len(post_list)):
      owner = bloguser.objects.get(id=post_list[i].owner_id)
      dictionary["title{0}".format(i+1)]=post_list[i].title
      dictionary["editor_name{0}".format(i+1)]= "{0} {1}".format(owner.name,owner.surname)
      dictionary["date{0}".format(i+1)]=post_list[i].created
      dictionary["post_text{0}".format(i+1)]=post_list[i].content
   return dictionary
   
#--------------------------------------------
""" Eshed Sorosky 
      7/DEC/21
      return bloguser object page  """
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
   if request.method == 'GET':
      path = "SCE_Proj/template/homepage-XXX.html"
      post_list = get_post_list(request,0,"homepage","")
      if verify_cookie(request):
         dbuser = get_bloguser_ob(request)
         dbrole = dbuser.role
         path = path.replace("XXX",dbrole)
         response_dict = {    #for showing user data
                                                "name":dbuser.name,
                                                "surname":dbuser.surname,
                                                "email":dbuser.email,
                                                "nickname":dbuser.nickname,
                                                "role":dbrole}
         response_dict.update(create_post_dict(request,post_list))
         response = render(request,path,response_dict)
         return response
      else:
         response_dict = create_post_dict(request,post_list)
         path = path.replace("XXX","guest")
      return render(request,path,response_dict)
   elif request.method == 'POST':
      form = search_form(request.POST)
      if form.is_valid():
        return search_view(request,form)
      else:
         form = search_form()
         return redirect('homepage')
#--------------------------------------------
"""   Eshed Sorosky 
      6/JAN/22
      return search page """
def search_view(request):
   path = "SCE_Proj/template/search.html"
   if request.method == 'GET':
      response = render(request,path)
      response.set_cookie('page',0)
      return response
   elif request.method == 'POST':
      if 'search' in request.POST:
         pass


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
      if form.is_valid():
         dbuser = get_bloguser_ob(request)
         if form.cleaned_data.get('name')!=None and form.cleaned_data.get('name')!="":               
            dbuser.name = form.cleaned_data.get('name')
         if form.cleaned_data.get('surname') and form.cleaned_data.get('surname')!="":
            dbuser.surname = form.cleaned_data.get('surname')
         if form.cleaned_data.get('nickname') and form.cleaned_data.get('nickname')!="":
            dbuser.nickname = form.cleaned_data.get('nickname')
         if form.cleaned_data.get('bio') and form.cleaned_data.get('bio')!="":
            dbuser.bio = form.cleaned_data.get('bio')
         if form.cleaned_data.get('old_pass') !=None:
            if(form.cleaned_data.get('old_pass')== dbuser.password):
               if(form.cleaned_data.get('password')!=None and form.cleaned_data.get('confirmpass')!= None):
                  if(form.cleaned_data.get('password') == form.cleaned_data.get('confirmpass')):
                     dbuser.password = form.cleaned_data.get('password')
                  else:
                     form = settings_info()
                     return render(request,'SCE_Proj/template/setting_page.html',
                     {
                        'fullname':"{0} {1}".format(dbuser.name,dbuser.surname),
                        'firstname':dbuser.name,
                        'lastname':dbuser.surname,
                        'nickname':dbuser.nickname,
                        'bio':dbuser.bio,
                        'email':dbuser.email,
                     })
         dbuser.save()
         return render(request,'SCE_Proj/template/setting_page.html',
         {
            'fullname':"{0} {1}".format(dbuser.name,dbuser.surname),
            'firstname':dbuser.name,
            'lastname':dbuser.surname,
            'nickname':dbuser.nickname,
            'bio':dbuser.bio,
            'email':dbuser.email,
         })
   if request.method == 'GET':
      if verify_cookie(request):
         dbuser = get_bloguser_ob(request)
         return render(request,'SCE_Proj/template/setting_page.html',
         {
            'fullname':"{0} {1}".format(dbuser.name,dbuser.surname),
            'firstname':dbuser.name,
            'lastname':dbuser.surname,
            'nickname':dbuser.nickname,
            'bio':dbuser.bio,
            'email':dbuser.email,
         })
      return redirect('login')
#--------------------------------------------
"""   Mor Bar 
      3/JAN/22
      return createpost page  """
def createpost(request):
   if request.method == 'GET':
      if verify_cookie(request):
         dbuser = get_bloguser_ob(request)
         if(dbuser.role == 'editor'):
            return render(request,"SCE_Proj/template/createpost.html")
         else:
            redirect('homepage')
      else:
         redirect('login')
   elif request.method == 'POST':
      if verify_cookie(request):
         dbuser = get_bloguser_ob(request)
         if dbuser.role == 'editor':
            form = new_post(request.POST)
            form.is_valid()
            if form.is_valid():
               post = Post(
                  title = form.cleaned_data.get('title'),
                  tags = form.cleaned_data.get('tags'),
                  content = form.cleaned_data.get('content'),
                  owner = dbuser
               )
               post.save()
               return redirect('homepage')
            else:
               form = new_post()
               return render(request,"SCE_Proj/template/createpost.html")
         else:
            return redirect('homepage')
      else:
         return redirect('login')
#--------------------------------------------
"""   Eshed Sorotsky 
      3/JAN/22
      return logout page  """
def logout(request):
   if request.method == 'GET':
      if verify_cookie(request):
         return render(request,"SCE_Proj/template/log_out.html")
      else:
         return redirect('landingpage')
   elif request.method == 'POST':
      if verify_cookie(request):
         if 'logout' in request.POST:
            response = redirect('landingpage')
            response.delete_cookie('email')
            response.delete_cookie('last_connection')
            return response
      else:
         return redirect('landingpage')
#--------------------------------------------
"""   Eshed Sorotsky 
      6/JAN/22
      return become editor page  """
def become_editor(request):
   path = "SCE_Proj/template/become_editor.html"
   if verify_cookie(request):
      dbuser = get_bloguser_ob(request)
      if dbuser.role != 'registered':
         return redirect('homepage')
      else:
         if request.method == 'GET':
            return render(request,path)
         elif request.method == 'POST':
            return HttpResponse('temp')       
   else:
      return redirect('login')