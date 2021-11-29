from django.db import models

# Create your models here.
#   Created by Eshed Sorotsky
#   29/NOV/21
#the users model, general for registered,editor & administrator
class User(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)
    nickname = models.CharField(max_length = 20,unique = True)
    email = models.EmailField(max_length = 50,unique = True)
    role = models.CharField(max_length = 10)
    picture = models.ImageField(default = None,upload_to=None, height_field=None, width_field=None, max_length=100)
    #1 to many relation for all the posts the user posted
    posts = models.ForeignKey('Post',default = 1,on_delete=models.CASCADE)
    #1 to many relation for all the comments the user made
    comments = models.ForeignKey('Comment',default = 1,on_delete = models.CASCADE)
    created = models.DateField(auto_now = False,auto_now_add = False)

    class Meta:
        db_table = "User"

#posts class
class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    tags = models.CharField(max_length = 250,default = None)
    #1 to many consisting of all the ratings
    ratings = models.ForeignKey('Rating',default = 1,on_delete = models.CASCADE)
    #1 to many consisting of all the comments of a certain post
    comments = models.ForeignKey('Comment',default = 1,on_delete=models.CASCADE)
    #1 to 1 relation for the post owner
    owner = models.OneToOneField('User',default = 1,on_delete=models.CASCADE)
    created = models.DateField(auto_now = False,auto_now_add = False)
    class Meta:
        db_table = "Post"

#comments class
class Comment(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField(max_length = 100)
    #1 to 1 relation for the comment owner
    owner = models.OneToOneField('User',default = 1,on_delete=models.CASCADE)
    created = models.DateField(auto_now = False,auto_now_add = False)
    class Meta:
        db_table = "Comment"

#Rating class
class Rating(models.Model):
    star = models.DecimalField(max_digits = 1,decimal_places = 1)
    created = models.DateField(auto_now = False,auto_now_add = False)
