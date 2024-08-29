from django.db import models
# from datetime import datetime
# Create your models here.
# makemigrations = create  changes and store in a file
# migrate = apply the pending the changes by migrations
class Contact (models.Model):
    # sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=60)
    phone =models.CharField(max_length=10)
    desc = models.TextField()
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return (" Name: "+self.name)

  
class User (models.Model):
   
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=60)
    phone =models.CharField(max_length=10)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return (" Name: "+self.name)

class Profile(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (" User: "+self.user.name)
    
