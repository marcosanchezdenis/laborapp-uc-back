from rest_framework import serializers
from location.models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id','address1','address2','latitude','longitude')