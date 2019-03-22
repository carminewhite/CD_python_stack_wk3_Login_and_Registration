from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email already exists in the database"
        if len(postData['fname']) <  2:
            errors["first_name"] = "First name should have at least 2 characters"
        if len(postData['lname']) <  2:
            errors["last_name"] = "Lastr name should have at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email not in a valid format"
        if len(postData['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters"
        if postData['confirm_password'] != postData['password']:
            errors["password"] = "Passwords don't match"
        return errors

    def login_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['login_email']):
            errors["login_email"] = "Email not in a valid format"
        if len(postData['login_password']) < 8:
            errors["login_password"] = "Password incorrect"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
