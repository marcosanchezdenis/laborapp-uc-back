from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from data.models import * 
#from provider.models import *
from privacy.models import *
from data.models import *


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data =  models.ManyToManyField(Property,through='CustomerData')
    providers = models.ManyToManyField('provider.Provider',blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.user)

class CustomerData(models.Model):
    customer =  models.ForeignKey(Customer,related_name="customer_data", on_delete=models.CASCADE)
    property =  models.ForeignKey(Property,on_delete=models.CASCADE)
    visibility =  models.ManyToManyField('privacy.Visibility',blank=True)
    value =  models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)