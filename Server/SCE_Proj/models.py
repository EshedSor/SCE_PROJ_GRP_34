from django.db import models

# Create your models here.
#   28/NOV/21
class User(models.Model):
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    type = models.CharField(max_length = 10)
    
    class Meta:
        db_table = "User"
        