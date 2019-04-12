from rest_framework import serializers
from score.models import *
from score.serializers import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill 
        fields = ('id','name','description')

class ScoreSystemValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreSystemValue
        fields = ('id','textual','value')

class ScoreSystemSerializer(serializers.ModelSerializer):
    systems =  ScoreSystemValueSerializer(many=True)
    class Meta:
        model = ScoreSystem 
        fields = ('id','name','description', 'systems')



class ScoreProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ScoreProvider 
        skill =  SkillSerializer()
        score_system = ScoreSystemSerializer()
        score_system_value = ScoreSystemValueSerializer()
        fields = ('id','skill','score_system','score_system_value')

class ScoreCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreCustomer   
        skill =  SkillSerializer()
        score_system = ScoreSystemSerializer()
        score_system_value =  ScoreSystemValueSerializer()
        fields = ('id','skill','score_system','score_system_value') 