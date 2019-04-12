from django.db import models

# Create your models here.

class Location (models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    def __str__(self):
        return '%s, %s' % (self.address1,self.address2)