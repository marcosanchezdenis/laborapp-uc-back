from django.shortcuts import render
from rest_framework import viewsets,generics



from customer.models import * 
from customer.serializers import *

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset =  Customer.objects.all()
    serializer_class =  CustomerSerializer


class CustomerDataViewSet(viewsets.ModelViewSet):
    queryset =  CustomerData.objects.all()
    serializer_class =  CustomerDataSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class =  UserSerializer



class SearchProviderViewSet(generics.ListAPIView):
    queryset =  Provider.objects.all()
    serializer_class =  ProviderSerializer



