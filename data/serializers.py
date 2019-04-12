
from rest_framework import serializers
from data.models import *

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ('id','name')

class PropertySerializer(serializers.ModelSerializer):
    type = PropertyTypeSerializer()
    class Meta:
        
        model = Property 
        fields = ('id','name','description','type','required', 'control_type')