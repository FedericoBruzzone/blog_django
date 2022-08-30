from distutils.command.upload import upload
from email import header
import this
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding') # default='uncategorized'
    snippet = models.CharField(max_length=255)# default='Click Link Above To Read Blog Post...'
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author) 

    def get_absolute_url(self):
        #return reverse('article_detail', args=(str(self.id)))
        return reverse('home')

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, blank=True)
    linkedin_url = models.CharField(max_length=255, blank=True)
    indeed_url = models.CharField(max_length=255, blank=True)
    facebook_url = models.CharField(max_length=255, blank=True)
    twitter_url = models.CharField(max_length=255, blank=True)
    instagram_url = models.CharField(max_length=255, blank=True)
    pinterest_url = models.CharField(max_length=255, blank=True)



    def __str__(self):
        return str(self.user)