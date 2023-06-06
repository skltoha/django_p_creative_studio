from django.db import models


# Create your models here.
class contactus(models.Model):
    client_email    = models.EmailField(max_length=100)
    client_name     = models.CharField(max_length=100)
    client_message  = models.TextField(max_length=500)
    
    
class team(models.Model):
    name = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = "images/")
    designation = models.CharField(max_length=30)
    info = models.TextField(max_length=200)
    facebook = models.URLField(max_length=200, null=True)
    instagram = models.URLField(max_length=200, null=True)
    dropbox = models.URLField(max_length=200, null=True)
    twitter = models.URLField(max_length=200, null=True)


class clientsay(models.Model):
    name       = models.CharField(max_length=100)
    comments   = models.TextField(max_length=200)
    img        = models.ImageField(upload_to='images/')
    
    