from django.db import models
from django.contrib.auth.models import User

from customer.models import Customer 
from provider.models import Provider 







class RequestState(models.Model):
    name =  models.CharField(max_length=200)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Request(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    provider =  models.ForeignKey(Provider,related_name="requests",on_delete=models.CASCADE)
    state = models.ForeignKey(RequestState,on_delete=models.CASCADE) 
    message = models.TextField()
    requested_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    request =  models.ForeignKey(Request, on_delete=models.CASCADE, related_name="messages")
    