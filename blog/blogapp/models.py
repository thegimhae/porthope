from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here.


# Event model

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=255)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email = models.EmailField('Email Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey('Venue', blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name

    def all_events(request):
        event_list = Event.objects.all()
        return event_list

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    # title_tag = models.CharField(max_length=255, default="posting")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='letter')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absoulte_url(self):
        return reverse('home')
