from django.db import models
from django import forms
# Create your models here.
class portfolio(models.Model):
    title= models.CharField(max_length=100)
    desc = models.TextField()
    catg = models.CharField(max_length=5)
    slug = models.SlugField(default="", null=False)
    time = models.DateTimeField(blank=True,auto_now_add=True)
    imgs = models.FileField(upload_to='portfolio')
  

    def __str__(self):
        return self.title #show by tittle name 
class profile(models.Model):
    img = models.FileField(upload_to='profile')
    bgimg = models.FileField(upload_to='profile')

   