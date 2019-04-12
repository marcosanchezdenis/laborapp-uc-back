from rest_framework import serializers

from customer.models import *
from provider.models import *
from serviceRequest.models import* 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name' )



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service 
        fields = []


class ProviderDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProviderData 
        fields =  ['value', 'property', 'id']


class ProviderSerializer(serializers.ModelSerializer):
    provider_data = ProviderDataSerializer(many=True)
    class Meta:
        model =  Provider
        fields = ['service', 'provider_data'] 



class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Problem 
        fields = [ 'id' ,'name', 'description']




class RequestStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestState 
        fields =  ['id','name', 'description']





#only necessary information to select the service
class ProviderSearchSerializer(serializers.ModelSerializer):
    service =  ServiceSerializer()
    provider = ProviderSerializer()
    #providerdataSerializer only  property value, score of the provider
    class Meta:
        model = Provider 
        fields = [ 'service','provider_data', ]

class ProviderProfileSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    problems = ProblemSerializer(many=True)
    provider_data  = ProviderDataSerializer(many=True) 

    class Meta:
        model = Provider
        fields = [ 'service', "problems","provider_data" ]

class RequestProviderSerializer(serializers.ModelSerializer):
    #user will be passed in the view
    #provider is part of the request
    #state will be set in the view as the default state of send o pendient
    
    class Meta:
        model =  Request 
        fields = [ 'message', 'requested_date']

class CommentProviderSerializer(serializers.ModelSerializer):
    #user will be passed by the view

    class Meta:
        model = Comment 
        fields = ['text']


#is a provider feature 
class MyServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider 
        fields = ['user ','service','problems', 'comments', 'requests', "provider_data"]




class MyRequestSerializer(serializers.ModelSerializer):
    #state serializer 
    #provider serializer
    provider =  ProviderSerializer()
    state = RequestStateSerializer()

    class Meta:
        model = Request 
        fields = [ 'provider', 'state', 'message', 'requested_date', 'messages', 'id' ]


#it may be
#class MyRequestsSerializer(serializer.ModelSerializer):
#    class Meta:
#        model = Resquest
#        fields = [] 


class RequestMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message 
        fields = [ 'text',] 


class MyRequestStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request 
        fields = ['state']











class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username' ]

class CustomerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData 
        fields =  ('id','customer','property','visibility','value')

        
class CustomerSerializer(serializers.ModelSerializer):
    customer_data = CustomerDataSerializer(many=True)
    class Meta:
        model = Customer 
        fields = ('id','user','customer_data','providers')



class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Provider
        fields = ['service','provider_data']

