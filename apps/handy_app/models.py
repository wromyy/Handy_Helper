from __future__ import unicode_literals
import datetime 
from django.db import models
# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        email_match = User.objects.filter(email=postData['email'])
        if len(email_match) > 0:
            errors['email'] = "Email is already taken"
        if len(postData['fname']) < 2:
            errors['fname'] = "First name has to be more than 2 characters"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last name has to be more than two characters"
        if len(postData['passwordsignup']) < 5:
            errors['passwordsignup'] = "Password has to be more than 5 characters"
        if not postData['passwordsignup_confirm'] == postData['passwordsignup']:
            errors['passwordsignup_confirm'] = "Passwords have to match"
        return errors

    def login_validator(self, postData):
        errors = {}
        login_user = User.objects.filter(email=postData['email'])
        if len(login_user) == 0:
            errors['login'] = "Invalid login"
        elif not postData['password'] == login_user[0].password:
            errors['login'] = "Invalid login"
        return errors

class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Job name must be greater than 3 characters"
        if len(postData['location']) == 0:
            errors['location'] = "Location cant be blank"
        if len(postData['description']) == 0:
            errors['description'] = "Description can't be blank" 
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Job(models.Model):
    job_todo = models.ManyToManyField(User, related_name="dojob")
    User = models.ForeignKey(User, related_name="jobs", on_delete=models.PROTECT)
    title = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager() 

class Category(models.Model):
    Job = models.ManyToManyField(Job, related_name="categories")
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


