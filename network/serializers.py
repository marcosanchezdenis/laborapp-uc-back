from network.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from django.core.exceptions import ValidationError


from django.db.models import Q
"""
class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ()
"""



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username','email', 'first_name','last_name']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username','password','email']

        
    password = serializers.CharField(write_only=True)

    def create(self,validated_data):
        username =  validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User.objects.create(
            username =  username,
            email = email,

        )
        user_obj.set_password(password)
        user_obj.save()

        return user_obj



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=True)
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):

        user_obj = None
        email =  data.get('email')
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(
            Q(email = email) 
        )
        if user.exists() and user.count() == 1 :
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid ")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Password.")

        data['user'] = user_obj
        data['info'] = user
        return data
        

    





class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)



class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType 
        fields = ('id','name',)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields =  ('id','type','value','user')
















