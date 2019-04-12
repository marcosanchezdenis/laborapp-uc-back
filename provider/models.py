from django.db import models

from customer.models import *
from data.models import * 

from django.contrib.auth.models import User


class Problem(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.name)
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.name)



class Provider(models.Model):
    data =  models.ManyToManyField(Property,through="ProviderData")
    service =  models.ForeignKey(Service,on_delete=models.CASCADE)
    problems = models.ManyToManyField(Problem)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customers =  models.ManyToManyField(Customer,blank=True)

    color = models.CharField(max_length=200)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)


class Comment(models.Model):
    text =  models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    provider =  models.ForeignKey(Provider, on_delete=models.CASCADE,related_name="comments")


class ProviderData(models.Model):
    provider =  models.ForeignKey(Provider,related_name="provider_data",on_delete=models.CASCADE)
    property =  models.ForeignKey(Property,on_delete=models.CASCADE)
    visibility =  models.ManyToManyField('privacy.Visibility',blank=True)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)