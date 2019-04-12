from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User 
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST




from rest_framework.permissions import AllowAny

from network.models import *
from network.serializers import *



from django.conf.urls import url





class UserInfoView(APIView):
    serializer_class =  UserDetailSerializer
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class =  UserCreateSerializer
    queryset = User.objects.all() 



from django.contrib.auth import login
from rest_framework.authtoken.models import Token


class UserLoginAPIView(APIView):
    permission_class =  [AllowAny]
    serializer_class =  UserLoginSerializer

    

    def post(self, request, *args, **kargs):
        data = request.data
        user_serializer =  UserLoginSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        user =  user_serializer.validated_data['user']
        login(request, user)
        userdata =  UserDetailSerializer(user)
        token, created =  Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user": userdata.data}, status=200)


from rest_framework.authentication import TokenAuthentication

class LogoutView(APIView):
    authentication_class =  (TokenAuthentication, )
    
    def post(self,request):
        logout(request)
        return Response(status=204)







class CityViewSet(viewsets.ModelViewSet):
    queryset =  City.objects.all()
    serializer_class = CitySerializer

class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer












