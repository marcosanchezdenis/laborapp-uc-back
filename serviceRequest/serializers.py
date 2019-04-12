from rest_framework import serializers
from serviceRequest.models import *

from provider.models import *








class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name' )





class RequestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service 
        fields = ('id', 'name' ,'description')
        
class ProviderDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderData
        fields = ('id','property','value')


class RequestProviderSerializer(serializers.ModelSerializer):
    service =  RequestServiceSerializer()
    provider_data =  ProviderDataSerializer(many=True)
    class Meta:
        model = Provider 
        fields =  ('id', 'provider_data', 'service','color')








class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    provider = RequestProviderSerializer()

    class Meta:
        model= Message 
        fields = [ 'text', 'user', 'provider', 'created_at']





class RequestStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestState 
        fields = ('id','name','description')

class RequestSerializer(serializers.ModelSerializer):
    user =  UserSerializer()
    provider = RequestProviderSerializer()
    state =  RequestStateSerializer()
    messages = MessageSerializer(many=True,required=False)

    class Meta:
        model =  Request 
        fields =  ('id','provider','user','state','message','requested_date', 'messages')

    def create(self, validated_data):
        customer =  validated_data.pop('user')
        state = validated_data.pop('state')

        return Request.objects.create( user=User.objects.get(pk=1), state=RequestState.objects.get(pk=1), **validated_data)
