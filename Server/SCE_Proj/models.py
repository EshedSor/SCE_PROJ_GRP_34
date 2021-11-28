from django.db import models

# Create your models here.
#   Created by Eshed Sorotsky
#   29/NOV/21
#the users model, general for registered,editor & administrator
class User(models.Model):
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)
    nickname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    role = models.CharField(max_length = 10)
    #1 to many relation for all the posts the user posted
    posts = models.ForeignKey('Post',default = 1)
    #1 to many relation for all the comments the user made
    class Meta:
        db_table = "User"

#posts class
class Post(models.Model):
    title = models.CharField(max_length = 30)
    #1 to many consisting of all the comments of a certain post
    comments = models.ForeignKey('Comment',default = 1)
    #1 to 1 relation for the post owner
    owner = models.OneToOneField('User',default = 1)
    class Meta:
        db_table = "Post"

#comments class
class Comment(models.Model):
    title = models.CharField(max_length = 30)
    #1 to 1 relation for the comment owner
    owner = models.OneToOneField('User',default = 1)
    class Meta:
        db_table = "Comment"