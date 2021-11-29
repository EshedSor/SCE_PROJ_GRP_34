from django.db import models

# Create your models here.
#   Created by Eshed Sorotsky
#   29/NOV/21
#the blogusers model, general for registered,editor & administrator
class tmp(models.Model):
    email = models.EmailField(max_length = 50,unique = True)
    password = models.CharField(max_length = 30)
    class Meta:
        db_table = "tmp"
class bloguser(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20,default = '')
    password = models.CharField(max_length = 30)
    nickname = models.CharField(max_length = 20,unique = True,default = '')
    email = models.EmailField(max_length = 50,unique = True)
    role = models.CharField(max_length = 10,default = 'registered')
    #picture = models.ImageField(default = None,upload_to=None, height_field=None, width_field=None, max_length=100)
    #1 to many relation for all the posts the bloguser posted
    posts = models.ForeignKey('Post',default = 1,on_delete=models.CASCADE)
    #1 to many relation for all the comments the bloguser made
    comments = models.ForeignKey('Comment',default = 1,on_delete = models.CASCADE)
    #created = models.DateTimeField(auto_now_add = False)

    class Meta:
        db_table = "bloguser"

#posts class
class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    tags = models.CharField(max_length = 250,default = None)
    #1 to many consisting of all the ratings
    ratings = models.ForeignKey('Rating',default = 1,on_delete = models.CASCADE)
    #1 to many consisting of all the comments of a certain post
    comments = models.ForeignKey('Comment',default = None,on_delete=models.CASCADE)
    #1 to 1 relation for the post owner
    owner = models.OneToOneField('bloguser',default = None,on_delete=models.CASCADE)
    #created = models.DateTimeField(auto_now_add = False)
    class Meta:
        db_table = "Post"

#comments class
class Comment(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField(max_length = 100)
    #1 to 1 relation for the comment owner
    owner = models.OneToOneField('bloguser',default = None,on_delete=models.CASCADE)
   # created = models.DateTimeField(auto_now_add = False)
    class Meta:
        db_table = "Comment"

#Rating class
class Rating(models.Model):
    star = models.DecimalField(max_digits = 1,decimal_places = 1)
    #created = models.DateTimeField(auto_now_add = False)
    class Meta:
        db_table = "Rating"
