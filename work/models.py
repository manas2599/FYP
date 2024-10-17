from django.db import models
from datetime import date
from datetime import timedelta
from datetime import datetime

# Create your models here.


class login(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150, default='password')
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.email


class signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150, default='password')
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.name


class Bugs(models.Model):
    company_name = models.CharField(max_length=100)
    website_url = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pricing = models.CharField(max_length=100)
    comments = models.CharField(max_length=1200)

    def __str__(self):
        return self.company_name
