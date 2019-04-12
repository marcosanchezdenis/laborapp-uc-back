from rest_framework import serializers

from customer.models import *
from provider.models import *



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

