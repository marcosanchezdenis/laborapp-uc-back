from django.db import models

# Create your models here.

class Search(models.Model):



    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)