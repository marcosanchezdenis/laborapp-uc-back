from rest_framework import serializers

from customer.serializers import *
from provider.models import *
from privacy.serializers import *
from serviceRequest.serializers import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['first_name','last_name','id']


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem 
        fields = ('id','name', 'description')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment 
        fields = ['text','user','created_at']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service 
        fields = ('id','name','description')

class ProviderDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderData
        fields = ('id','property','visibility','value')

class ProviderSerializer(serializers.ModelSerializer):
    provider_data =  ProviderDataSerializer(many=True)
    service = ServiceSerializer(required=False)
    problems = ProblemSerializer(many=True, required=False)
    
    requests  = RequestSerializer(many=True)
    comments = CommentSerializer(many=True)
    user =  UserSerializer()
    class Meta:
        model =  Provider 
        fields =  ('id','provider_data','service','user','problems','requests','color', 'comments')
    
    def create(self,  validated_data):
        provider_data =  validated_data.pop('provider_data')
        problems = validated_data.pop('problems')
        service = validated_data.pop('service')
        customers =  []
        print(problems)
        
        #create provider
        #TODO add user request 
        provider = Provider.objects.create(user=User.objects.get(pk=1),service=service) #service=Service.objects.get(pk=1)

        #provider assign service
        provider.service = service
        
        #provider add problem
        for problem in problems:
           
            provider.problems.add(problem)
        #provider add provider_data
        for data in provider_data:
            provider_data = ProviderData.objects.create(provider=provider,**data)
        
            


        return provider





