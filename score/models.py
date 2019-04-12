from django.db import models


from customer.models import Customer
from provider.models import Provider 



class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScoreSystem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class ScoreSystemValue(models.Model):
    textual = models.CharField(max_length=200)
    value  = models.IntegerField()
    system = models.ForeignKey(ScoreSystem,on_delete=models.CASCADE, related_name="systems")
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScoreProvider(models.Model):
    #skill =  models.ForeignKey(Skill,on_delete=models.CASCADE)
    score_system = models.ForeignKey(ScoreSystem,on_delete=models.CASCADE)
    score_system_value = models.ForeignKey(ScoreSystemValue,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

class ScoreCustomer(models.Model):
    skill =  models.ForeignKey(Skill,on_delete=models.CASCADE)
    score_system =  models.ForeignKey(ScoreSystem,on_delete=models.CASCADE)
    score_system_value =  models.ForeignKey(ScoreSystemValue,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)



