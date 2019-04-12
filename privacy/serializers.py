from rest_framework import *
from privacy.models import *


class AbstractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abstraction 
        fields = ('id','name','description','property','level','process_id')

class VisibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Visibility 
        abstraction = Abstraction
        fields =  ('id','context_type','abstraccion') 