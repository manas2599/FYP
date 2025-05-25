from django.db import models
from datetime import date
from datetime import timedelta
from datetime import datetime
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import base64
import os


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

# models.py


class EncryptedFile(models.Model):
    file = models.FileField(upload_to='static/assets/images/')  # File saved in static
    filename = models.CharField(max_length=255, null=True)
    encrypted_key = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.encrypted_key