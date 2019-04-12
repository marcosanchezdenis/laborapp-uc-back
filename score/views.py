from rest_framework import serializers,viewsets 

from score.models import *
from score.serializers import *




class SkillViewSet(viewsets.ModelViewSet):
 
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ScoreSystemViewSet(viewsets.ModelViewSet):
    queryset = ScoreSystem.objects.all()
    serializer_class =  ScoreSystemSerializer

class ScoreSystemValueViewSet(viewsets.ModelViewSet):
    queryset = ScoreSystemValue.objects.all()
    serializer_class = ScoreSystemValueSerializer



