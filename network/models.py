from django.db import models

from django.contrib.auth.models import User

# Create your models here.


from rest_framework import serializers
from django.contrib.auth.models import User






class City(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.name)

class ContactType(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.name)



class Contact(models.Model):   
    type  = models.ForeignKey(ContactType,on_delete=models.CASCADE)
    value = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s, %s' % (self.type, self.value)








