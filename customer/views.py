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

#list of providers of customer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProviderSearch(APIView):
    def get(self,request, format=None):
        provider =  Provider.objects.all() # provider that aprove the data shared of the system
        serializer =  ProviderSerializer(provider,many=True)
        return Response(serializer.data)

class ProviderProfile(APIView):
    def get(self,request,pk, format=None):
        provider = Provider.objects.get(pk=pk)# check if the provider accepts to shared data
        serializer = ProviderProfileSerializer(provider)
        return Response(serializer.data)


class RequestProvider(APIView):
    def post(self,request,pk, format=None):
        provider = Provider.objects.get(pk=pk)
        serializer = RequestProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(provider=provider,user=request.user,state=RequestState.objects.get(pk=1))
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)



class CommentProvider(APIView):
    def post(self,request,pk, format=None):
        provider = Provider.objects.get(pk=pk)
        serializer= CommentProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, provider=provider)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)








#class MyServices(APIView):
#    def get(self,request,format=None):
#        provider = Provider.objects.all()
#        serializer =  MyServicesSerializer(provider,many=True)
#        return Response(serializer.data) """

from rest_framework.permissions import IsAuthenticated
class MyRequests(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request, format=None):
        request = Request.objects.filter(user=request.user)
        serializer =  MyRequestSerializer(request,many=True)
        return Response(serializer.data)

class MyRequest(APIView):
    def get(self,request, pk,format=None):
        request = Request.objects.filter(user=request.user, pk=pk)
        serializer =  MyRequestSerializer(request)
        return Response(serializer.data)


class MyRequestMessages(APIView):
    def get(self,request,pk, format=None):
        messages = Message.objects.filter(request=pk) #verify that request belong the user
        serializer = RequestMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self,request,pk, format=None):
        req = Request.objects.get(pk=pk)
        serializer =  RequestMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, request= req)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class MyRequestState(APIView):
    #to change the state of states
    def put(self,request,pk, format=None):
        request = Request.objects.get(pk=pk)
        serializer = MyRequestStateSerializer(request,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



