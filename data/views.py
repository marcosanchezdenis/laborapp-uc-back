from rest_framework import serializers,viewsets 
from data.models import *

from data.serializers import *


class PropertyViewSet(viewsets.ModelViewSet):
    queryset =  Property.objects.all()
    serializer_class =  PropertySerializer


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
