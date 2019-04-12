from django.shortcuts import render

from rest_framework import viewsets

from provider.models import *
from provider.serializers import * 


# Create your views here.
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def perform_create(self, instance):
        instance.save(user= self.request.user)


class ProviderDataViewSet(viewsets.ModelViewSet):
    queryset =  ProviderData.objects.all()
    serializer_class = ProviderDataSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



